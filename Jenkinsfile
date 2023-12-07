pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sudipta-Das007/Capstone-2.git'
            }
        }
        
        stage('Build Images') {
            steps {
                script {
                    bat 'docker build -t image_cap_app .'
                }
            }
        }

        stage('Push Images to Hub') {
            steps {
                withDockerRegistry([ credentialsId: "", url: "" ]) {
                    bat 'docker push image_cap_app'
                }
            }
        }

        stage('Deploy App') {
            steps {
                script {
                    bat 'docker run -p 8088:8088 -e ML_ENDPOINT=http://ml-service:5000 image_cap_app'
                }
            }
        }
    }

    post {
        always {
            /* This block will always be executed, regardless of the build result */
            bat 'docker logout'
        }

        failure {
            emailext(
                attachLog: true,
                body: '''<html>
                        <p>The build failed. Please check the Jenkins console output for details.</p>
                        <p>Build URL: ${BUILD_URL}</p>
                        </html>''',
                subject: 'Build Failure',
                to: 'nimit.singhal20@st.niituniversity.in, manjim.sarkar20@st.niituniversity.in,anirudh.sharma20@st.niituniversity.in, sudipta.das20@st.niituniversity.in',
                mimeType: 'text/html'
            )
        }

        success {
            emailext(
                attachLog: true,
                body: 'The build was successful.',
                subject: 'Build Success',
                to: 'nimit.singhal20@st.niituniversity.in, manjim.sarkar20@st.niituniversity.in,anirudh.sharma20@st.niituniversity.in, sudipta.das20@st.niituniversity.in',
                mimeType: 'text/html'
            )
        }
    }
}
