// Fonction qui permet de d'envoyer sur une autre page si les ids sont bons
$(document).ready(function(){
    function idCheck(){

        $.ajax({
            // Place here the final server url
            url: 'http://192.168.1.11:8000/index',
            dataType: 'jsonp',
            jsonp: 'jsoncallback',
            timeout: 5000,
            success: function(data, status){
                console.log(data);
                $.each(data, function(i,item){
                    if (item.resultat == 'success'){
                        window.location="connexion.html";
                    }
                    if (item.resultat == 'mauvais mdp'){
                        alert('Mauvaise combinaison identifiant/mot de passe.');
                    }
                    if (item.resultat == 'noID'){
                        alert('Identifiant non enregistré, veuillez créer un compte.');
                    }
                });
            },
            error: function(){
                console.log(data);
                alert('Pas de connexion au serveur.');
            }
        });
    }
});



// Fonction qui permet de vérifier que tout a bien été intégré en base de donnée
$(document).ready(function(){
    function formulaireCheck(){

        $.ajax({
            // Place here the final server url
            url: 'http://192.168.1.11:8000/index',
            dataType: 'jsonp',
            jsonp: 'jsoncallback',
            timeout: 5000,
            success: function(data, status){
                console.log(data);
                $.each(data, function(i,item){
                    if (item.resultat == 'success'){
                        window.location="connexion.html";
                    }
                    if (item.resultat == 'mauvais mdp'){
                        alert('Mauvaise combinaison identifiant/mot de passe.');
                    }
                    if (item.resultat == 'noID'){
                        alert('Identifiant non enregistré, veuillez créer un compte.');
                    }
                });
            },
            error: function(){
                console.log(data);
                alert('Pas de connexion au serveur.');
            }
        });
    }
});


// Fonction qui permet d'envoyer les données au serveur
$(document).bind('deviceready', function(){
    $(function(){
        $('form').submit(function(e){
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
            
            //alert('envoie des données');
            //window.location="connexion.html";

            $.ajax({
                type: 'POST',
                dataType: "json",
                data: JSON.stringify(data),//+'&lid='+landmarkID,
                // Place here the final server url
                url: 'http://192.168.1.11:8000/index.py',
                success: function(data){
                    console.log(data);
                    if (page.data == 'connexion'){
                        idCheck();
                    }
                    if (page.data == 'formulaire'){
                        formulaireCheck();
                        // Balises pour placer le code d'Aude et Caroline : envoie calendrier
                        // Début
                        // Fin
                    }
                },
                error: function(){
                    console.log(data);
                    alert('Pas de connexion au serveur.');
                }
            });
            return false;
        });
    });
});
