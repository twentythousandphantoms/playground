import subprocess
import logging

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("deployment.log")
    ]
)
logger = logging.getLogger(__name__)


def create_eks_cluster():
    logger.info("Creating EKS cluster using Terraform...")
    try:
        subprocess.run(["terraform", "init"], check=True)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        logger.info("EKS cluster created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Error creating EKS cluster. Exiting...")
        logger.exception(e)
        exit(1)


def configure_kubectl():
    logger.info("Configuring kubectl...")
    try:
        # Use AWS CLI to configure kubectl with EKS cluster credentials
        subprocess.run(["aws", "eks", "update-kubeconfig", "--name", "exness-eks", "--region", "us-west-2"], check=True)
        logger.info("kubectl configuration completed.")
    except subprocess.CalledProcessError as e:
        logger.error("Error configuring kubectl. Exiting...")
        logger.exception(e)
        exit(1)


def apply_kubernetes_manifests():
    logger.info("Applying Kubernetes manifests...")
    try:
        # Use kubectl to apply Nginx and PHP backend Deployment and Service manifests
        subprocess.run(["kubectl", "apply", "-f", "php-service.yaml"], check=True)
        subprocess.run(["kubectl", "apply", "-f", "php-pvc.yaml"], check=True)
        subprocess.run(["kubectl", "apply", "-f", "php-deployment.yaml"], check=True)
        subprocess.run(["kubectl", "apply", "-f", "nginx-cm.yaml"], check=True)
        subprocess.run(["kubectl", "apply", "-f", "nginx-deployment.yaml"], check=True)
        logger.info("Kubernetes manifests applied successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Error applying Kubernetes manifests. Exiting...")
        logger.exception(e)
        exit(1)


if __name__ == "__main__":
    try:
        create_eks_cluster()
        configure_kubectl()
        apply_kubernetes_manifests()
    except Exception as e:
        logger.error("An unexpected error occurred during deployment. Exiting...")
        logger.exception(e)
        exit(1)
