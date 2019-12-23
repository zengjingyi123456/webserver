$(document).ready(function(){


  const chart = new G2.Chart({
    container: 'c1',
    width : 1200,
    height : 600
  });
  chart.source(dataInfo);
  chart.interval().position('genre*sold').color('genre')
  chart.render();

  const chart1 = new G2.Chart({
    container: 'c2',
    width : 1200,
    height : 600
  });
  chart1.source(dataInfo1);
  chart1.interval().position('genre*sold').color('genre')
  chart1.render();

  const chart2 = new G2.Chart({
    container: 'c3',
    width : 1200,
    height : 600
  });

  chart2.source(dataInfo2);
  chart2.interval().position('genre*sold').color('genre')
  chart2.render();

  const chart3 = new G2.Chart({
    container: 'c4',
    width : 1200,
    height : 600
  });

  chart3.source(dataInfo3);
  chart3.interval().position('genre*sold').color('genre')
  chart3.render();

  const chart4 = new G2.Chart({
    container: 'c5',
    width : 1200,
    height : 600
  });

  chart4.source(dataInfo4);
  chart4.interval().position('genre*sold').color('genre')
  chart4.render();

  const chart5 = new G2.Chart({
    container: 'c6',
    width : 1200,
    height : 600
  });

  chart5.source(dataInfo5);
  chart5.interval().position('genre*sold').color('genre')
  chart5.render();

  const chart6 = new G2.Chart({
    container: 'c7',
    width : 1200,
    height : 600
  });

  chart6.source(dataInfo6);
  chart6.interval().position('genre*sold').color('genre')
  chart6.render();

});
