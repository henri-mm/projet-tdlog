// Fonction qui permet de d'envoyer sur une autre page si les ids sont bons
$(document).ready(function(){
    function idCheck(){

        $.ajax({
            // Place here the final server url
            url: 'http://localhost:3000/index.py',
            dataType: 'jsonp',
            jsonp: 'jsoncallback',
            timeout: 5000,
            success: function(data, status){
                console.log(data);
                $.each(data, function(i,item){
                    if (item.connexion == 'OK'){
                        window.location="connexion.html";
                    };
                    if (item.connexion == 'KO'){
                        alert('Mauvaise combinaison identifiant/mot de passe.');
                    };
                    if (item.connexion == 'noID'){
                        alert('Identifiant non enregistré, veuillez créer un compte.');
                    };
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
        $('form').submit(function(){
            // Ligne indiquant de quel formulaire le json
            var landmarkID = $(this).parent().attr('bloc_page');
            var postData = $(this).serialize();

            $.ajax({
                type: 'POST',
                data: postData+'&lid='+landmarkID,
                // Place here the final server url
                url: 'http://localhost:3000/index.py',
                success: function(data){
                    console.log(data);
                    idCheck();
                    // Balises pour placer le code d'Aude et Caroline...
                    // Début
                    // Fin
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
