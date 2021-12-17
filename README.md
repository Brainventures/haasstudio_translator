# 번역 Pipeline

### **0. 순서** : 문장 입력 -> 사전 번역 -> 문장 번역

### **1. 라이브러리 설치**

```shell
prompt> sh install_libs.sh
```

### **2. Models Download**

- 리눅스/Mac 사용 시 : `prompt> sh download_models.sh`
- 그 외 : [다운로드](https://drive.google.com/file/d/19lcFLwa2NNGi7ATLRUy6nZfarMqULMop/view?usp=sharing)
- 다운로드 받은 후 해당 폴더(translate_pipeline)에 압축 해제

### **3. Run streamlit**

```shell
streamlit run translate_pipeline.py
```

<br/><br/>

## 화면 예시

![image](https://user-images.githubusercontent.com/52812181/141072396-2ef2d462-5a3e-4f89-b37f-90dadd7144ac.png)