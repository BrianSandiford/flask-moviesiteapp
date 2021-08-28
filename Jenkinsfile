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
    
}