# Is ROC-AUC sensitive to "class imbalance"?
Depends on what we mean by class imbalance, but for the case simulated here, the answer is no. 

![Image](https://shottr-uploads.s3.amazonaws.com/TDZ559SG8KS4GCCG/TMOn-SCR-20221108-l72.png?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASHY5OHU5UIVLCXXR%2F20221108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221108T141624Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=bfafba1f813e32ad64121983c991aead2c467af3a4c134ba4a9d298ae07918b2)

## A simple example
# Receiver operating characteristics (ROC)
ROC-AUC is a function of sens and spec. If sens/spec are unchanged, so is ROC-AUC.

Say you have this 2x2 table:
![Img2](https://shottr-uploads.s3.amazonaws.com/TDZ559SG8KS4GCCG/T3UZ-SCR-20221108-lhf.png?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASHY5OHU5UIVLCXXR%2F20221108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221108T142808Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=ec64c2bc54319685f0ef6a9d97ce43724483427e275a2bd0927d037414e786fe)

Let's say you "fix" this class imbalace by down-sampling true-negatives 1:10:
![Img](https://shottr-uploads.s3.amazonaws.com/TDZ559SG8KS4GCCG/TKNM-SCR-20221108-lgx.png?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASHY5OHU5UIVLCXXR%2F20221108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221108T142747Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=bcf517f5eed7d8fc5a391d4b60f97210078aeddefb6f0b74739f659608b938e6)

Sens and spec are unchanged, thus ROC-AUC is unchanged.
See also simulation on GitHub [here](https://github.com/MartinBernstorff/ROC-AUC-simulation.git).