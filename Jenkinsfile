pipeline{
    agent any
    environment {
        Dockerhub_user="DOCKER USERNAME"
        App_name="chatwhiz"
        IMAGE_TAG="${BUILD_NUMBER}"
        IMAGE_NAME="${Dockerhub_user}" + "/" + "${App_name}"
        REGISTRY_CRED = "docker-token"
        

    }
    
    stages{
        stage("Checkout SCM"){
            steps{
                withCredentials([gitUsernamePassword(credentialsId: 'git-token', gitToolName: 'Default')]) {
                    
                }      
            }
        }

        stage("Build Docker Image")
        {
            steps{
                script{
                    docker_image= docker.build "${IMAGE_NAME}"
                }
            }
        }
        stage("Push Docker Image")
        {
            steps{
                script
                {
                    withCredentials([usernamePassword(credentialsId: 'docker-token', passwordVariable: 'Password', usernameVariable: 'Username')]) {
                        
                    sh "docker login -u '$Username' -p '$Password'"
                    }

                    sh """docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:latest
                    docker image push ${IMAGE_NAME}:latest
                    docker image push ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker rmi ${IMAGE_NAME}:latest
                    docker rmi ${IMAGE_NAME}:${BUILD_NUMBER}"""
                    
                    }
                }
            }
        stage("Updating Kubernetes Files")
        {
            steps{
                script{
                    sh """
                    cat deployment.yml
                    sed -i 's/${App_name}.*/${App_name}:${IMAGE_TAG}/g ' deployment.yml
                    cat deployment.yml
                    
                    
                    """
                }
            }
        }
        stage("Trigger CD")
        {
            steps
            {
                script{
                    echo 'Triggered CD using ArgoCD'
                }
            }
        }
        }
    }
