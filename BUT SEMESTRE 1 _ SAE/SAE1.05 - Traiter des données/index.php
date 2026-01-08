<!DOCTYPE HTML>
<html>
<head>
<script>
window.onload = function() {

//variable contenant les valeurs à afficher dans le graphique
var dataPoints = [];

//voir https://canvasjs.com/docs/charts/basics-of-creating-html5-chart/ pour plus d'options
var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "dark1", //le thème du graphique. Valeurs possibles : “light1″,”light2”, “dark1”, “dark2” 
	title: { 
		text: "Voici le nombre de décès par mois " //le titre du graphique
	},
	axisX: {
		title: "Les mois" //le titre de l'axe des X
		
	},
	axisY: {
		title: "Nombre de décès ",  //le titre de l'axe des Y
		includeZero: true // L'axe des Y doit il commencer à 0 ? (true,false)
	},
	data: [{
		type: "column", //le type de graphique voir https://canvasjs.com/docs/charts/chart-types/ (valeurs conseillées : line,stepLine,spline,area,bar,column,pie,doughnut )
		yValueFormatString: "## décès", //le format d'affichage des infobulles. Ici 2 chiffres après la virgule suivui du texte "grumfa"
		dataPoints: dataPoints 
	}]
});

/*la fonction qui permet de lire le contenu du fichier userdata.json.
chaque donnée doit être au format : 
 {
    "x": 3,            ici, 3 est la valeur de x
    "y": 5,            ici 5 est la valeur de y
    "label": "titi"    SI vous voulez faire apparaître un label, il faut renseigner cette ligne.
  },
*/
function addData(data) {
	for (var i = 0; i < data.length; i++) {
		dataPoints.push({
			x: data[i].x,
			y: data[i].y,
			indexLabel:data[i].label
		});
	}
	chart.render();

}
//Ouverture du fichier 'userdata.json' et lancement de la fonction 'addData'
$.getJSON("./userdata.json", addData);

}
</script>
</head>
<body>

	Le graphique ci-dessous représente le nombre de décès total par mois en 2019 :
<p></p>






<!-- On crée un 'div' qui contiendra le graphique-->
<div id="chartContainer" style="height: 370px; width: 100%;"></div>

<!-- On ajoute les librairies nécessaires pour gérer le graphique -->
<script src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"></script>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>


