/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
<<<<<<< HEAD
};
=======
});


// Fonction qui permet d'envoyer les données au serveur
$(document).bind('deviceready', function(){
    $(function(){
        $('#connexion').submit(function(e){
            // Empécher l'envoi par défaut
            e.preventDefault();
            
            // Ligne indiquant de quel formulaire le json
            //var landmarkID = $(this).parent().attr('bloc_page');
            //var postData = $(this).serializeArray();
            var data = {};
            var Form = this;
            
            $.each(this.elements, function(i,v){
                var input = $(v);
                data[input.attr("name")] =  input.val();
                delete data["undefined"];
            });
            alert(data);
            
            //alert('envoie des données');
            //window.location="accueil.html";
            $.post('http://192.168.1.11:8000/index/', $(this).serialize(), function(data){ idCheck();});
            //$.ajax({
            //    type: "POST",
            //    dataType: "json",
            //    contentType: "application/json",
            //    data: JSON.stringify(data),//+'&lid='+landmarkID,
            //    // Place here the final server url
            //    url: "http://192.168.1.11:8000/index",
            //    success: function(data){
            //        console.log(data);
            //        if (page.data == 'connexion'){
            //            idCheck();
            //        }
            //        if (page.data == 'formulaire'){
            //            formulaireCheck();

                        // Balises pour placer le code d'Aude et Caroline : envoie calendrier
                        // Début
			// if (window.plugins.calendar.hasReadWritePermission == false){
				// window.plugins.calendar.requestReadWritePermission;
			// }
			// window.plugins.calendar.createEvent('Rendre objet','Ponts', 'Oublie pas ;)', startDate, endDate, success, error);
                        // Fin
            //        }
            //    },
            //    error: function(){
            //        console.log(data);
            //        alert('Pas de connexion au serveur.');
            //    }
            //});
            return false;
        });
    });
});
>>>>>>> d8c3d3b5a4e532213a0a339757f12f3d76ff7197
