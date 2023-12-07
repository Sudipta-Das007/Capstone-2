pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('nimit-dockerhub')
        DOCKER_IMAGE_NAME = 'nimitsinghal/capstone:Image_cap'
        DOCKER_EXE_PATH = 'C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe'
        CURRENT_STAGE = ''
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        CURRENT_STAGE = 'Checkout'
                        // Checkout the code from your GitHub repository
                        checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/Sudipta-Das007/Capstone-2.git']]])
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Checkout stage failed: ${e.message}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    CURRENT_STAGE = 'Build'
                    // Build the Docker image
                    bat "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }

        stage('Login') {
    steps {
        script {
            CURRENT_STAGE = 'Login'
            // Log in to Docker Hub
            withCredentials([usernamePassword(credentialsId: 'nimit-dockerhub', usernameVariable: 'nimitsinghal', passwordVariable: 'dckr_pat_5gfh5DM75WFd0RztxfCOQ_Z9sx4')]) {
            }
        }
    }
}

stage('Push') {
    steps {
        script {
            CURRENT_STAGE = 'Push'
            // Push the Docker image to Docker Hub
            withDockerRegistry([ credentialsId: 'nimit-dockerhub', url: 'https://index.docker.io/v1/' ]) {
                bat "docker push nimitsinghal/capstone:Image_cap"
                
            }
        }
    }
}


        stage('Test') {
            steps {
                script {
                    CURRENT_STAGE = 'Test'
                    echo 'Tests are complete'
                }
            }
            post {
                always {
                    script {
                        // Send email notification for this stage with log attachment
                        emailext (
                            to: 'nimit.singhal20@st.niituniversity.in, nimit.singhal02@gmail.com',
                            subject: "Jenkins Build ${currentBuild.result}: ${env.JOB_NAME} - #${env.BUILD_NUMBER}",
                            body: """
                            <p>Build Status: ${currentBuild.result}</p>
                            <p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                            <p>Current Stage: ${CURRENT_STAGE}</p>
                            ${currentBuild.result == 'FAILURE' ? '<p>Failed Stage: ${CURRENT_STAGE}</p>' : ''}
                            """,
                            attachLog: true
                        )
                    }
                }
            }
        }
    }
}
