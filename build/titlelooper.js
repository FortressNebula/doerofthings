import { animate, scrambleText } from 'https://cdn.jsdelivr.net/npm/animejs/+esm';

const doer = document.getElementById("doer");
const things = document.getElementById("things");

const doers = [
	"doer",
	"prover",
	"fewer",

	"doer",
	"loser",
	"lurer",

	"doer",
	"user",
	"cooler",
	
	"doer",
	"brewer",
	"sewer",

	"doer",
	"plougher",
	"flower",

	"doer",
	"bluer",
	"gluer",
];

const thingses = [
	"things",
	"links",
	"these",

	"things",
	"keys",
	"fish",

	"things",
	"trees",
	"cheese",

	"things",
	"paint",
	"tricks",

	"things",
	"fields",
	"teals",

	"things",
	"greens",
	"sheets",
]

let i = 0;

function loop() {
	i = (i + 1) % doers.length;
	animate(doer, {
		innerText: scrambleText({ 
			text: doers[i],
			chars: 'lowercase',
			revealRate: 10, 
			settleRate: 20,
			revealDelay: 300,
		}),
	});

	animate(things, {
		innerText: scrambleText({ 
			text: thingses[i],
			chars: 'lowercase',
			revealRate: 10, 
			settleRate: 20,
			delay: 300,
			revealDelay: 300,
		}),
	});
}

setInterval(loop, 4000);