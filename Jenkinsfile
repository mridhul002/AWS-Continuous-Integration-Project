pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS =   // Jenkins credential ID
        IMAGE_NAME = "your_dockerhub_username/calculator-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mridhul002/AWS-CONTINUOUS-INTEGRATION-PROJECT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    // replace with your EC2 details
                    def EC2_IP = "ec2-xx-xx-xx-xx.compute-1.amazonaws.com"
                    def PEM_PATH = "/home/ubuntu/jenkins-key.pem"
                    
                    sh """
                    ssh -o StrictHostKeyChecking=no -i ${PEM_PATH} ubuntu@${EC2_IP} '
                        docker pull ${IMAGE_NAME}:latest &&
                        docker stop calculator || true &&
                        docker rm calculator || true &&
                        docker run -d -p 5000:5000 --name calculator ${IMAGE_NAME}:latest
                    '
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}
