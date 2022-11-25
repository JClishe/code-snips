terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.10.0"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = "53191582-ab8f-4451-96c8-995f7d00123b"
  # tenant_id = "7c17-75bd-427b81d2-8b31-171ea6c31427" 
}
