# ESC-50 Urban Noise Analysis: Environmental Sound & Mental Health Impact

## Abstract
This project presents a comprehensive analysis of urban noise pollution leveraging the ESC-50 environmental sound dataset. By employing advanced machine learning — particularly Random Forest algorithms — it predicts mental health impacts arising from diverse urban sounds. The model combines WHO noise guidelines, audio feature engineering, and health risk assessment to offer valuable insights for urban planning and public health.

## Problem Statement
Urban environments are increasingly plagued by noise pollution impacting mental well-being. Traditional approaches lack granular analysis linking specific urban sound types to health outcomes. This project addresses this gap by developing a machine learning pipeline to classify urban sounds and quantify associated mental health risks, enabling targeted interventions and smarter city designs.

## Advantages
- **Comprehensive Coverage:** Utilizes 2000+ samples across 50 diverse environmental sound categories (ESC-50 dataset).
- **Domain-Informed Modeling:** Integrates WHO noise exposure norms with psychoacoustic and health metrics.
- **Advanced Machine Learning:** Employs Random Forest for robust classification and regression, delivering high accuracy and interpretability.
- **Health Impact Estimation:** Predicts continuous mental health impact scores with contextual risk stratification.
- **Visual Insights:** Provides professional-grade, interactive dashboards highlighting noise distribution and health correlations.
- **Extensible & Reproducible:** Modular codebase suitable for extension and adaptation to other environmental datasets.
- **Platform Compatible:** Fully operational across Windows, macOS, and Linux with simplified setup instructions.

## Architecture Diagram
![Architecture diagram](./docs/architecture-diagram.png)
*Note: Architecture highlights data flow starting from raw ESC-50 loading → feature engineering → health impact modeling → Random Forest classification/regression → visualization & reporting.*

## Project Structure
ESC-50 Urban Noise Analysis/
├── Config/
│ └── config.py # Centralized configuration & constants
├── data/
│ ├── dataset.py # Dataset download & preprocessing script
│ └── esc50_dataset.csv # ESC-50 dataset metadata (CSV)
├── logs/ # Log files (training & execution)
├── models/
│ ├── esc50_classifier.pkl # Pretrained ESC-50 Random Forest classifier
│ ├── health_regressor_esc50.pkl # Pretrained Random Forest regressor for health
│ ├── rf_classifier.pkl # Additional Random Forest classifier models
│ └── rf_regressor.pkl # Additional regression models
├── results/
│ ├── visualizations/
│ │ └── clean_dashboard.png # Generated analysis dashboard
│ └── rf_analysis_results.csv # Final processed results
├── Config/
│ ├── init.py # Config package file
│ └── config.py # Configurations
├── demo.py # Interactive demo to run entire pipeline & visualize results
├── sampleDataset.py # Dataset exploration and preview script
├── test_project.py # End-to-end test suite for codebase validation
├── urban_noise_analyzer.py # Core ML pipeline and domain logic
├── .gitignore # Git ignore specification
├── requirements.txt # Python dependencies list
└── README.md # Project documentation & overview

## Project Initialization
### Step 1: Dataset Download
The ESC-50 dataset metadata CSV is downloaded programmatically from the official [ESC-50 GitHub repository](https://github.com/karolpiczak/ESC-50). Audio files can be downloaded separately as guided in the ESC-50 repo.
python data/dataset.py

### Step 2: Dataset Preview
Quick data exploration and confirmation of dataset integrity:
python sampleDataset.py

### Step 3: Run Full Demo
Execute the full analysis pipeline, including model training, health impact assessment, and dashboard generation:
python demo.py

### Step 4: Results Output
All results including the processed dataset, trained models, and professional dashboards save automatically under:

- [`demo.py`](./demo.py) — Interactive demo script you ran  
- [`demo_output`](./demo_output) — Output folder containing summarized results and visuals  
- [`README.md`](./README.md) — This detailed documentation  
- `.gitignore` — Clean project versioning ignoring large files and outputs  
- [`requirements.txt`](./requirements.txt) — Environment dependencies  

Note: demo file consists all imported files from its original code file.

## Conclusion
This project effectively bridges environmental sound classification and public health by quantifying mental health impacts arising from urban noise pollution. The robust Random Forest models deliver reliable predictions validated through cross-validation and comprehensive testing. The interactive dashboards make the intricate data and results accessible and actionable for data scientists, urban planners, and health professionals alike.

## Future Work

- **Deep Learning Expansion:** Integration of CNN-based audio feature extraction for improved sound classification.  
- **Real-time Monitoring:** Development of streaming pipelines for live urban noise analysis using sensor networks.  
- **Expanded Health Metrics:** Incorporate physiological sensor data (e.g., heart rate, cortisol) for personalized health impact modeling.  
- **Policy Simulation:** Scenario analysis to guide noise mitigation policies and urban design adaptations.  
- **Cross-Dataset Generalization:** Adapting the pipeline for other sound pollution datasets and multilingual environments.

## Disclaimer
*The source code of this project is not publicly shared at this time due to confidentiality agreements rather demo file is shared to get an idea for implementation. Interested parties may contact the author via email for access requests and collaboration inquiries.*

## License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## Contact
- **Email:** mdshabbi885@gmail.com  
- **GitHub:** [github.com/Mahaboobunnisa123](https://github.com/Mahaboobunnisa123)  
