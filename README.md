# Healthcare Content Engine

B2B/B2C content generation and marketing automation framework for healthcare, medical devices, pharmaceuticals, and biotech companies.

## 🎯 Overview

This framework automates the process of creating compliant, data-driven content for healthcare audiences. Built with healthcare marketing best practices and designed to scale across multiple channels (email, social, web, ads).

## 🏥 Supported Industries

* Medical device distribution
* Pharmaceutical companies
* Biotech & genetic testing services
* Healthcare providers & clinics
* MedTech startups

## 🚀 Key Features

### B2B Content Generation
* Compliance-first: All content templates follow FDA/medical content guidelines
* Lead nurture sequences: Automated multi-touch campaigns
* Thought leadership: Case studies, whitepapers, webinars
* Sales enablement: Battle cards, product overviews

### B2C Content Generation
* Patient education: Symptom guides, treatment explanations
* Health tips: Preventive care content
* Call-to-action optimization: Conversion-focused messaging
* Multi-language support: Localized content

### Marketing Automation
* Lead scoring: Behavioral + firmographic signals
* Email sequences: Triggered workflows based on stage
* Social media: Content calendar with scheduling
* Analytics: Attribution, cohort analysis, KPI tracking

## 📊 Architecture
[Content Generator] → [Template Engine] → [Multi-Channel Distributor]
↓                    ↓                        ↓
[B2B Logic]      [Healthcare Rules]      [Email/SMS/Social]
[B2C Logic]      [Compliance Check]      [Analytics Tracking]
## 🔧 Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/healthcare-content-engine.git
cd healthcare-content-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r config/requirements.txt
```

## 📖 Usage

### Generate B2B Content

```python
from src.content.b2b_generator import B2BContentGenerator

generator = B2BContentGenerator()
content = generator.generate(
    industry="medical_device",
    topic="clinical_efficacy",
    audience="hospital_administrators",
    format="email"
)
print(content)
```

### Run Email Nurture Workflow

```python
from src.workflows.email_sequence import EmailNurtureFlow

workflow = EmailNurtureFlow()
workflow.configure(
    stage="awareness",
    duration_days=14,
    audience_segment="high_intent_prospects"
)
workflow.execute()
```

### Track Campaign Performance

```python
from src.analytics.performance_tracker import PerformanceTracker

tracker = PerformanceTracker()
metrics = tracker.get_campaign_metrics(
    campaign_id="pharma_q2_2026",
    date_range="last_30d"
)
print(metrics)
```

## 📚 Documentation

* [Architecture](docs/architecture.md)
* [API Guide](docs/api-guide.md)
* [Deployment](docs/deployment.md)
* [Examples](examples/)

## 💼 Case Studies

* [Medical Device B2B Campaign](examples/medical_device_campaign.md)
  * Result: 35% improvement in lead quality score
  * Focus: Compliance + technical accuracy
  
* [Pharmaceutical Lead Nurture](examples/pharmaceutical_nurture.md)
  * Result: 3.2x increase in conversion rate
  * Focus: Educational + trust-building

## 🧪 Testing

```bash
# Run all tests
bash scripts/run_tests.sh

# Run specific test
python -m pytest tests/test_b2b_content.py
```

## 🔐 Security & Compliance

* ✅ HIPAA-aware data handling
* ✅ FDA guideline compliance (for claims)
* ✅ Email marketing compliance (CAN-SPAM, GDPR)
* ✅ No patient PII in templates

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📈 Roadmap

- [ ] Multi-language support (Spanish, Vietnamese)
- [ ] AI-powered personalization
- [ ] Healthcare provider API integration
- [ ] Advanced attribution modeling
- [ ] Real-time A/B testing framework

## 📄 License

MIT License - see LICENSE file

## ✍️ Author

**Phuc Sinh**  
Digital Marketing | Growth Strategy  
[LinkedIn](https://www.linkedin.com/in/phuc-sinh-le/) | [Facebook](https://www.facebook.com/phucsinhlee/)

---

*Last updated: April 2026*
