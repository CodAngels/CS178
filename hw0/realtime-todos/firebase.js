import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

var firebaseConfig = {
    apiKey: "AIzaSyA6-q6G3gkxPteHMkOKoIo1BqbtcK7lvFc",
    authDomain: "todolist-app-72f27.firebaseapp.com",
    projectId: "todolist-app-72f27",
    storageBucket: "todolist-app-72f27.appspot.com",
    messagingSenderId: "200913793496",
    appId: "1:200913793496:web:834538499b1c84d47382ad",
    measurementId: "G-YQ7ETGC2L7"
};
firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const googleProvider = new firebase.auth.GoogleAuthProvider();

export const db = firebase.firestore();