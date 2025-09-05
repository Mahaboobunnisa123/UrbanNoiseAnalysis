"""
🎯 URBAN NOISE ANALYSIS - DEMO
================================
ESC-50 Environmental Sound → Mental Health Impact Analysis
Using Random Forest Algorithm
"""

import os
import shutil
import warnings
import runpy

warnings.filterwarnings('ignore')


def quick_test():
    """Quick test to verify setup"""
    print("🧪 QUICK SETUP TEST")
    print("=" * 20)
    files_to_check = [
        os.path.join('Config', 'config.py'),
        'urban_noise_analyzer.py',
        os.path.join('data', 'dataset.py'),
        'sampleDataset.py'
    ]
    missing = []
    for f in files_to_check:
        if not os.path.isfile(f):
            print(f"❌ {f} missing")
            missing.append(f)
        else:
            print(f"✅ {f} found")
    return len(missing) == 0


def save_demo_results(analyzer, results):
    """Save results and dashboard to demo_output folder."""
    output_dir = 'demo_output'
    os.makedirs(output_dir, exist_ok=True)

    # Save results CSV
    results_file = os.path.join(output_dir, 'rf_analysis_results.csv')
    results.to_csv(results_file, index=False)
    print(f"✅ Saved analysis results to {results_file}")

    # Copy dashboard image
    src = os.path.join('results', 'visualizations', 'clean_rf_dashboard.png')
    dst = os.path.join(output_dir, 'clean_rf_dashboard.png')
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"✅ Copied dashboard to {dst}")
    else:
        print("⚠️ Dashboard image not found; run the analysis first.")


def main():
    """Run complete urban noise analysis demo"""

    print("🏙️ URBAN NOISE POLLUTION & MENTAL HEALTH ANALYSIS")
    print("=" * 55)
    print("📊 Dataset: ESC-50 (2000 samples, 50 sound categories)")
    print("🤖 Algorithm: Random Forest (Classifier + Regressor)")
    print("🎯 Goal: Analyze noise impact on mental health")
    print("=" * 55)

    # STEP 1: Download dataset script
    print("\n📥 STEP 1: Getting ESC-50 Dataset...")
    try:
        runpy.run_path(os.path.join('data', 'dataset.py'), run_name='__main__')
        print("✅ Dataset downloaded successfully!")
    except Exception as e:
        print(f"⚠️ Dataset download failed: {e}")

    # STEP 2: Dataset preview
    print("\n📊 STEP 2: Dataset Preview...")
    try:
        runpy.run_path('sampleDataset.py', run_name='__main__')
        print("✅ Dataset preview complete!")
    except Exception as e:
        print(f"⚠️ Sample preview failed: {e}")

    # STEP 3: Run complete analysis
    print("\n🤖 STEP 3: Running Complete Analysis...")
    try:
        from urban_noise_analyzer import RandomForestNoiseAnalyzer
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return

    analyzer = RandomForestNoiseAnalyzer()
    results = analyzer.run_complete_analysis()
    if results is None:
        print("❌ Analysis failed.")
        return

    # Display key results
    print("\n🎉 ANALYSIS COMPLETE!")
    class_acc = analyzer.training_history['classification']['test_accuracy']
    reg_r2 = analyzer.training_history['regression']['test_r2']
    reg_mae = analyzer.training_history['regression']['test_mae']
    print(f"📊 Classification Accuracy: {class_acc:.1%}")
    print(f"📊 Health Prediction R²: {reg_r2:.3f}")
    print(f"📊 Prediction MAE: ±{reg_mae:.1f} points")
    print(f"📂 Files: models/, results/, demo_output/")

    # Save outputs to demo_output
    save_demo_results(analyzer, results)


if __name__ == "__main__":
    print("🎯 URBAN NOISE ANALYSIS DEMO")
    print("1) Quick Test  2) Full Demo")
    choice = input("Enter choice (1/2): ").strip()
    if choice == "1":
        quick_test()
    elif choice == "2":
        if quick_test():
            print("\n" + "="*50)
            main()
        else:
            print("❌ Setup incomplete.")
    else:
        print("❌ Invalid choice.")
