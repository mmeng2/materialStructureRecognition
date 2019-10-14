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
    },
    getRecognizeTableList() {
        return new Promise((resolve, reject) => {
            axios.get("/getRecognizeTableList/", {})
                .then(result => {
                    resolve(result);
                })
                .catch(error => {
                    reject(error);
                });
        });
    },
    getRecognizedCardList() {
        return new Promise((resolve, reject) => {
            axios.get("/getRecognizedCardList/", {})
                .then(result => {
                    resolve(result);
                })
                .catch(error => {
                    reject(error);
                });
        });
    },
    getRecognizedDetail(params) {
        // return new Promise((resolve, reject) => {
        //     axios.post("//", params)
        //         .then(result => {
        //             resolve(result);
        //         })
        //         .catch(error => {
        //             reject(error);
        //         });
        // });
    },
};

export default API
