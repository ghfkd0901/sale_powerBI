<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Power BI 대시보드</title>
  <style>
    body {
      display: flex;
      margin: 0;
      font-family: Arial, sans-serif;
    }
    .sidebar {
      width: 220px;
      background-color: #f4f4f4;
      padding: 20px;
      height: 100vh;
      box-shadow: 2px 0 5px rgba(0,0,0,0.1);
    }
    .sidebar h2 {
      font-size: 18px;
      margin-bottom: 20px;
    }
    .sidebar a {
      display: block;
      padding: 10px;
      margin-bottom: 10px;
      color: #333;
      text-decoration: none;
      border-radius: 5px;
    }
    .sidebar a:hover {
      background-color: #ddd;
    }
    .content {
      flex: 1;
      padding: 0;
    }
    iframe {
      border: none;
      width: 100%;
      height: 100vh;
    }
  </style>
</head>
<body>

  <div class="sidebar">
    <h2>📊 보고서 메뉴</h2>
    <a href="#" onclick="loadReport('customer')">고객별 당월/누계 분석</a>
    <a href="#" onclick="loadReport('product')">상품별 판매량 분석</a>
    <a href="#" onclick="loadReport('region')">지역별 연간 추이 분석</a>
  </div>

  <div class="content">
    <iframe id="reportFrame" src="https://app.powerbi.com/view?r=eyJrIjoiYjl...MID" title="Power BI"></iframe>
  </div>

  <script>
    const reportLinks = {
      customer: "https://app.powerbi.com/view?r=eyJrIjoiYjl...MID",
      product: "https://app.powerbi.com/view?r=eyJrIjoiXXX...XXX",
      region: "https://app.powerbi.com/view?r=eyJrIjoiZZZ...ZZZ"
    };

    function loadReport(key) {
      const iframe = document.getElementById('reportFrame');
      iframe.src = reportLinks[key];
    }
  </script>

</body>
</html>
