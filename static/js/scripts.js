/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})
    var ctx = document.getElementById("myChart").getContext("2d");

var xValues = ["1970s~1990s", "2000s", "2010s", "2020s"];
var yValues = [55, 49, 44, 24];
var barColors = ["#EB8AED", "#8D99F9","#8DF98D","#F9A659"];

const labels = ["1970s~1990s", "2000s", "2010s", "2020s"];

const data = {
  labels: labels,
  datasets: [
    {
      label: 'Happy',
      data: [42,14,40,4],
      backgroundColor: "#EB8AED",
      stack: 'Stack 0',
    },
    {
      label: 'Sad',
      data: [4,8,69,19],
      backgroundColor: "#8D99F9",
      stack: 'Stack 0',
    },
    {
      label: ['Energetic'],
      data: [0,39,61,0],
      backgroundColor: "#8DF98D",
      stack: 'Stack 0',
    },
        {
      label: 'Calm',
      data: [0,0,59,41],
      backgroundColor: "#F9A659",
      stack: 'Stack 0',
    },
  ]
};

new Chart(ctx, {
  type: "bar",
  data: data,
  
  options: {
    plugins: {
          title: {
            display: true,
            text: 'Chart.js Bar Chart - Stacked'
          },
        },
        responsive: true,
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
          },
              yAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Percentage(%)'
      }
    }]
        }
  }
});

// var ctx2 = document.getElementById("myPieChart").getContext("2d");

// new Chart(ctx2, {
//   type: "doughnut",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     title: {
//       display: true,
//       text: "World Wide Wine Production"
//     }
//   }
// });
    var ctx20 = document.getElementById("myChart20").getContext("2d");

var xValues = ["Happy", "Sad", "Calm", "Energetic"];
var yValues = [23, 42, 34, 64];
var barColors = ["#EB8AED", "#8D99F9","#8DF98D","#F9A659"];
const data2 = {
  labels: labels,
  datasets: [
    {
      label: 'Happy',
      data: [42,14,40,4],
      backgroundColor: "#EB8AED",
      stack: 'Stack 1',
    },
    {
      label: 'Sad',
      data: [4,8,69,19],
      backgroundColor: "#8D99F9",
      stack: 'Stack 2',
    },
    {
      label: ['Energetic'],
      data: [0,39,61,0],
      backgroundColor: "#8DF98D",
      stack: 'Stack 3',
    },
        {
      label: 'Calm',
      data: [0,0,59,41],
      backgroundColor: "#F9A659",
      stack: 'Stack 4',
    },
  ]
};

new Chart(ctx20, {
  type: "bar",
  data: data2,
  options: {
    plugins: {
          title: {
            display: true,
            text: 'Chart.js Bar Chart - Stacked'
          },
        },
        responsive: true,
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
          },
              yAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Percentage(%)'
      }
    }]
        }
  }
});
//     var ctx21 = document.getElementById("myChart21").getContext("2d");

// var xValues = ["Happy", "Sad", "Calm", "Energetic"];
// var yValues = [75, 39, 14, 24];
// var barColors = ["#EB8AED", "#8D99F9","#8DF98D","#F9A659"];

// new Chart(ctx21, {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//         legend: {display: false},
//     title: {
//       display: true,
//     }
//   }
// });
//     var ctx22 = document.getElementById("myChart22").getContext("2d");

// var xValues = ["Happy", "Sad", "Calm", "Energetic"];
// var yValues = [32, 71, 33, 28];
// var barColors = ["#EB8AED", "#8D99F9","#8DF98D","#F9A659"];

// new Chart(ctx22, {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//         legend: {display: false},
//     title: {
//       display: true,
//     }
//   }
// });
function myFunction() {
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");
console.log(moreText)

  if (btnText.style.display === "none") {
    console.log("Open")
    btnText.style.display = "inline";
    moreText.style.display = "none";

  } else {
    console.log("Open2")
    btnText.style.display = "none";
    moreText.style.display = "flex";

  }
}

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


