import axios from 'axios';
Vue.prototype.$http = axios;

function getTest() {
    axios.get("/test/", {})
        .then((response)=> {
            alert(response.data);
            console.log(response.data);
        })
        .catch(function (error) {
            console.log(error);
        })
}
