<script>
import { Line } from "vue-chartjs";


export default {
  extends: Line,
  mounted() {
    this.renderChart(

      {

        labels: [
          "8:30",
          "8:45",
          "9:00",
          "9:15",
          "9:30",
          "9:45",
          "Now"
        ],
        datasets: [
          {
            label: "Typowa tego dnia",
            data: [0,1,2,4,3,2],
            backgroundColor: "transparent",
            borderColor: "rgba(1, 116, 188, 0.50)",
            pointBackgroundColor: "rgba(171, 71, 188, 1)"
          },
           {
            label: "Dzisiejsza",
            data: [1,1,2,3,3,1],
            backgroundColor: "transparent",
            borderColor: "rgba(113, 16, 128, 0.50)",
            pointBackgroundColor: "rgba(121, 21, 18, 1)",

          }
        ]
      },
      {

        responsive: true,
        maintainAspectRatio: 2,
        title: {
          display: true,
          text: "Liczba oczekujących",
          fontSize: 50
        },
        labels:{
          fontSize: 50
        },
        scales:{
          xAxes:{
            ticks: {
                        barThickness: 18,
                        beginAtZero: true,
                        fontSize: 50,
                        fontColor: '#9E9E9E',
                    },
          },
          yAxes:{
            ticks: {
                        beginAtZero: true,
                        fontSize: 50,
                        fontColor: '#9E9E9E',
                    },
          }
        }

      }
    );
  }
};
</script>