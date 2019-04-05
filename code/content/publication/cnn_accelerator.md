+++
abstract = "We present a novel mechanism to accelerate state-of-art Convolutional Neural Networks (CNNs) on CPU-FPGA platform with coherent shared memory. First, we exploit Fast Fourier Transform (FFT) and Overlap-and-Add (OaA) to reduce the computational requirements of the convolutional layer. We map the frequency domain algorithms onto a highly-parallel OaA-based 2D convolver design on the FPGA. Then, we propose a novel data layout in shared memory for efficient data communication between the CPU and the FPGA. To reduce the memory access latency and sustain peak performance of the FPGA, our design employs double buffering. To reduce the inter-layer data remapping latency, we exploit concurrent processing on the CPU and the FPGA. Our approach can be applied to any kernel size less than the chosen FFT size with appropriate zero-padding leading to acceleration of a wide range of CNN models. We exploit the data parallelism of OaA-based 2D convolver and task parallelism to scale the overall system performance.\n By using OaA, the number of floating point operations is reduced by 39.14% ~ 54.10% for the state-of-art CNNs. We implement VGG16, AlexNet and GoogLeNet on Intel QuickAssist QPI FPGA Platform. These designs sustain 123.48 GFLOPs/sec, 83.00 GFLOPs/sec and 96.60 GFLOPs/sec, respectively. Compared with the state-of-the-art AlexNet implementation, our design achieves 1.35x GFLOPs/sec improvement using 3.33x less multipliers and 1.1x less memory. Compared with the state-of-art VGG16 implementation, our design has 0.66x GFLOPs/sec using 3.48x less multipliers without impacting the classification accuracy. For GoogLeNet implementation, our design achieves 5.56x improvement in performance compared with 16 threads running on a 10 Core Intel Xeon Processor at 2.8 GHz."
abstract_short = "We present a novel mechanism to accelerate state-of-art Convolutional Neural Networks (CNNs) on CPU-FPGA platform with coherent shared memory. First, we exploit Fast Fourier Transform (FFT) and Overlap-and-Add (OaA) to reduce the computational requirements of the convolutional layer. We map the frequency domain algorithms onto a highly-parallel OaA-based 2D convolver design on the FPGA. Then, we propose a novel data layout in shared memory for efficient data communication between the CPU and the FPGA. Our approach can be applied to any kernel size less than the chosen FFT size with appropriate zero-padding leading to acceleration of a wide range of CNN models. We exploit the data parallelism of OaA-based 2D convolver and task parallelism to scale the overall system performance."
authors = ["Chi Zhang", "Viktor Prasanna"]
date = "2017-02-22"
image_preview = ""
math = true
publication_types = ["1"]
publication = "ACM/SIGDA International Symposium on Field-Programmable Gate Arrays"
publication_short = "FPGA'17"
selected = true
title = "Frequency Domain Acceleration of Convolutional Neural Networks on CPU-FPGA Shared Memory System"
url_code = ""
url_dataset = ""
url_pdf = "http://ganges.usc.edu/svn/pg/pubs/preprint/fpga2017-zhang.pdf"
url_project = ""
url_slides = ""
url_video = ""

#[[url_custom]]
#name = "Custom Link"
#url = ""

# Optional featured image (relative to `static/img/` folder).
[header]
image = "headers/convolver.jpg"
caption = "" #"My caption :smile:"

+++


