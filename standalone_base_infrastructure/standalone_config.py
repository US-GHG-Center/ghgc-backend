"""Configuration options for optional stand-alone VPC Stack"""
from typing import Optional

from pydantic import BaseSettings, Field


class baseSettings(BaseSettings):
    """Settings for standalone base infrastructure"""

    base_name: Optional[str] = Field(
        "veda-shared",
        description="Optional name used to name stack and resources",
    )
    AWS_ACCOUNT_ID: Optional[str] = Field(
        None,
        description="When deploying from a local machine the AWS account id is required to deploy to an exiting VPC",
    )
    AWS_REGION: Optional[str] = Field(
        None,
        description="When deploying from a local machine the AWS region id is required to deploy to an exiting VPC",
    )

    vpc_cidr: Optional[str] = "10.100.0.0/16"
    vpc_max_azs: Optional[int] = 2
    vpc_nat_gateways: Optional[int] = 1

    def cdk_env(self) -> dict:
        """Load a cdk environment dict for stack"""
        return {
            "account": self.AWS_ACCOUNT_ID,
            "region": self.AWS_REGION,
        }

    class Config:
        """model config."""

        env_file = ".env"


base_settings = baseSettings()
