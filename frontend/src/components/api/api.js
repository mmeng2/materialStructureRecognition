import axios from 'axios';
import Vue from 'vue';

let API = {
  getTest() {
    return new Promise((resolve, reject) => {
      axios.get("/test/", {})
        .then(result => {
          resolve(result);
        })
        .catch(error => {
          reject(error);
        });
    });
  }
};

export default API
