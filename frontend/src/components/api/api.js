import axios from 'axios';
import Vue from 'vue';
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
