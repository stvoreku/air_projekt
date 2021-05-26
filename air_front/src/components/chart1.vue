<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  mounted() {
    this.renderChart(
      {
        labels: [
          "10:15",
          "10:30",
          "10:45",
          "11:00",
          "11:15",
          "11:30",
          "Now"
        ],
        datasets: [
          {
            label: "Typowa tego dnia",
            data: [6, 7, 8, 9, 7, 10, 11],
            backgroundColor: "transparent",
            borderColor: "rgba(1, 116, 188, 0.50)",
            pointBackgroundColor: "rgba(171, 71, 188, 1)"
          },
           {
            label: "Dzisiejsza",
            data: [4, 5, 6, 5, 8, 6, 4],
            backgroundColor: "transparent",
            borderColor: "rgba(113, 16, 128, 0.50)",
            pointBackgroundColor: "rgba(121, 21, 18, 1)"
          }
        ]
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: "Liczba oczekujących"
        }
      }
    );
  }
};
</script>