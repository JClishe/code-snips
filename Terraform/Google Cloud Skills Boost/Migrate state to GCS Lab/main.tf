provider "google" {
  project     = "qwiklabs-gcp-03-d2ecca2d1faa"
  region      = "us-central-1"
}
resource "google_storage_bucket" "test-bucket-for-state" {
  name        = "qwiklabs-gcp-03-d2ecca2d1faa"
  location    = "US"
  uniform_bucket_level_access = true
}

// Destination GCS bucket needs to already exist before using the code below
terraform {
  backend "gcs" {
    bucket  = "qwiklabs-gcp-03-d2ecca2d1faa"
    prefix  = "terraform/state"
  }
}

// Run "terraform init -migrate-state" to migrate the state