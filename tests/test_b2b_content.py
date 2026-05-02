"""Unit tests for B2B content generator"""

import pytest
from src.content.b2b_generator import (
    B2BContentGenerator,
    B2BContentRequest,
    HealthcareIndustry
)


class TestB2BContentGenerator:
    
    @pytest.fixture
    def generator(self):
        return B2BContentGenerator()
    
    def test_generate_medical_device_email(self, generator):
        """Test B2B email generation for medical device industry"""
        request = B2BContentRequest(
            industry=HealthcareIndustry.MEDICAL_DEVICE,
            topic="Surgical efficiency",
            audience_role="hospital_administrator",
            format="email"
        )
        
        content = generator.generate(request)
        
        assert content is not None
        assert len(content) > 100
        assert "compliance" in content.lower() or "fda" in content.lower()
    
    def test_compliance_validation_fails_for_invalid_claims(self, generator):
        """Test that invalid medical claims are caught"""
        request = B2BContentRequest(
            industry=HealthcareIndustry.PHARMACEUTICAL,
            topic="This drug cures cancer (unsubstantiated)",
            audience_role="doctor",
            format="email",
            compliance_level="fda_regulated"
        )
        
        with pytest.raises(ValueError):
            generator.generate(request)
    
    def test_template_selection_by_industry(self, generator):
        """Test that correct template is selected per industry"""
        for industry in HealthcareIndustry:
            request = B2BContentRequest(
                industry=industry,
                topic="Test topic",
                audience_role="test_role",
                format="email"
            )
            
            # Should not raise error
            content = generator.generate(request)
            assert content is not None
