node {
    def app
        stage('Cloning Git') {
            
              checkout scm     
            
        }
        
        stage('Testing') {
            
                script {
                  sh 'sh demo-selenium-test.sh'
        }
      
    }
         // Building Docker images
        stage('Building image') {
            
                script {
                  dockerImage = docker.build "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:"+env.BUILD_NUMBER
        }
      
    } 
}  