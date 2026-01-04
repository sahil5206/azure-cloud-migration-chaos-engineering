variable "location" {
  description = "Azure region"
  type        = string
  default     = "Central India"
}

variable "rg_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-fastapi-chaos"
}

variable "acr_name" {
  description = "Azure Container Registry name (must be globally unique)"
  type        = string
}

variable "aks_name" {
  description = "AKS cluster name"
  type        = string
  default     = "aks-fastapi-chaos"
}

variable "node_count" {
  description = "Number of nodes in default node pool"
  type        = number
  default     = 1
}

variable "node_size" {
  description = "VM size for AKS nodes"
  type        = string
  default     = "Standard_B2s_v2"
}


