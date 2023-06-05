# Biomedical_Data_Analysis
의생명 데이터 처리 및 실습 참고 코드 (과제 제외)

1. GO.py
Genomes.Orders의 유의미한 데이터를 뽑아주는 프로그램

./GO.py [path to Genomes.Order].Genomes.Order
<img width="1266" alt="image" src="https://github.com/Polaroidd/Biomedical_Data_Analysis/assets/101031710/9713f3c9-ed74-495a-996f-3f86fc5b746e">

2. find_by_id.py
id로 Conserved.Segments에서 id를 검색해주는 프로그램

./find_by_id.py [path to Conserved.Segments].Conserved.Segments [id of contig]
<img width="848" alt="image" src="https://github.com/Polaroidd/Biomedical_Data_Analysis/assets/101031710/8349a9d1-c891-4eec-81df-e9963a5e4e88">

3. seg_converter.py
contig 길이 최소값, chromosome 번호를 입력하여 해당하는 범위의 데이터들만 보여주는 프로그램

./find_by_id.py [path to Conserved.Segments].Conserved.Segments [min length of contig] [number of chromosome]
<img width="896" alt="image" src="https://github.com/Polaroidd/Biomedical_Data_Analysis/assets/101031710/cef18db0-cb9c-46da-9652-e436e049c52d">


4.split_inversion.py
GO.py의 결과 데이터를 바탕으로 연속되는 각각의 inversion 사이트들을 찾아주는 프로그램


./split_inversion.py [path to Conserved.Segments].Conserved.Segments
입력 : GO.py의 single contig data
<img width="1013" alt="image" src="https://github.com/Polaroidd/Biomedical_Data_Analysis/assets/101031710/4e8366f3-919b-46a4-af02-dcff0f33dbd6">


