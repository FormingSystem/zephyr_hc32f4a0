---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-4
title: imx_ccm_rev2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_imx\_ccm\_rev2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h.html)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>

```c
/*
 * Copyright 2021,2024-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV2_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV2_H_

/* Peripheral:
 *   range: 0 - 0xFF, starting from 0
 *
 * Instance:
 *   range: 0 - 0xFF, starting from 0
 */
#define IMX_CCM_PERIPHERAL_MASK        0xFF00UL
#define IMX_CCM_INSTANCE_MASK          0xFFUL

#define IMX_CCM_CORESYS_CLK            0
#define IMX_CCM_PLATFORM_CLK           0x1UL
#define IMX_CCM_BUS_CLK                0x2UL

/* Cortex-A55 core clock driven by ARM_PLL */
#define IMX_CCM_ARM_PLL_CLK 0x10UL

/* LPUART */
#define IMX_CCM_LPUART_CLK             0x300UL
#define IMX_CCM_LPUART1_CLK            0x300UL
#define IMX_CCM_LPUART0102_CLK         0x300UL
#define IMX_CCM_LPUART2_CLK            0x301UL
#define IMX_CCM_LPUART0304_CLK         0x301UL
#define IMX_CCM_LPUART3_CLK            0x302UL
#define IMX_CCM_LPUART0506_CLK         0x302UL
#define IMX_CCM_LPUART4_CLK            0x303UL
#define IMX_CCM_LPUART0708_CLK         0x303UL
#define IMX_CCM_LPUART5_CLK            0x304UL
#define IMX_CCM_LPUART0910_CLK         0x304UL
#define IMX_CCM_LPUART6_CLK            0x305UL
#define IMX_CCM_LPUART1112_CLK         0x305UL
#define IMX_CCM_LPUART7_CLK            0x306UL
#define IMX_CCM_LPUART8_CLK            0x307UL
#define IMX_CCM_LPUART9_CLK            0x308UL
#define IMX_CCM_LPUART10_CLK           0x309UL
#define IMX_CCM_LPUART11_CLK           0x30aUL
#define IMX_CCM_LPUART12_CLK           0x30bUL

/* LPI2C */
#define IMX_CCM_LPI2C_CLK              0x400UL
#define IMX_CCM_LPI2C0102_CLK          0x400UL
#define IMX_CCM_LPI2C1_CLK             0x400UL
#define IMX_CCM_LPI2C2_CLK             0x401UL
#define IMX_CCM_LPI2C0304_CLK          0x401UL
#define IMX_CCM_LPI2C3_CLK             0x402UL
#define IMX_CCM_LPI2C4_CLK             0x403UL
#define IMX_CCM_LPI2C0506_CLK          0x402UL
#define IMX_CCM_LPI2C5_CLK             0x404UL
#define IMX_CCM_LPI2C6_CLK             0x405UL
#define IMX_CCM_LPI2C0708_CLK          0x403UL
#define IMX_CCM_LPI2C7_CLK             0x406UL
#define IMX_CCM_LPI2C8_CLK             0x407UL

/* LPSPI */
#define IMX_CCM_LPSPI_CLK              0x500UL
#define IMX_CCM_LPSPI0102_CLK          0x500UL
#define IMX_CCM_LPSPI1_CLK             0x500UL
#define IMX_CCM_LPSPI2_CLK             0x501UL
#define IMX_CCM_LPSPI0304_CLK          0x501UL
#define IMX_CCM_LPSPI3_CLK             0x502UL
#define IMX_CCM_LPSPI4_CLK             0x503UL
#define IMX_CCM_LPSPI0506_CLK          0x502UL
#define IMX_CCM_LPSPI5_CLK             0x504UL
#define IMX_CCM_LPSPI6_CLK             0x505UL
#define IMX_CCM_LPSPI7_CLK             0x506UL
#define IMX_CCM_LPSPI8_CLK             0x507UL

/* USDHC */
#define IMX_CCM_USDHC1_CLK             0x600UL
#define IMX_CCM_USDHC2_CLK             0x601UL
#define IMX_CCM_USDHC3_CLK             0x602UL

/* DMA  */
#define IMX_CCM_EDMA_CLK               0x700UL
#define IMX_CCM_EDMA_LPSR_CLK          0x701UL
#define IMX_CCM_EDMA3_CLK              0x700UL
#define IMX_CCM_EDMA4_CLK              0x701UL

/* PWM */
#define IMX_CCM_PWM_CLK                0x800UL

/* CAN */
#define IMX_CCM_CAN_CLK                0x900UL
#define IMX_CCM_CAN1_CLK               0x900UL
#define IMX_CCM_CAN2_CLK               0x901UL
#define IMX_CCM_CAN3_CLK               0x902UL

/* GPT */
#define IMX_CCM_GPT_CLK                0x1000UL
#define IMX_CCM_GPT1_CLK               0x1000UL
#define IMX_CCM_GPT2_CLK               0x1001UL
#define IMX_CCM_GPT3_CLK               0x1002UL
#define IMX_CCM_GPT4_CLK               0x1003UL
#define IMX_CCM_GPT5_CLK               0x1004UL
#define IMX_CCM_GPT6_CLK               0x1005UL

/* SAI */
#define IMX_CCM_SAI1_CLK               0x1100UL
#define IMX_CCM_SAI2_CLK               0x1101UL
#define IMX_CCM_SAI3_CLK               0x1102UL
#define IMX_CCM_SAI4_CLK               0x1103UL

/* ENET */
#define IMX_CCM_ENET_CLK               0x1200UL
#define IMX_CCM_ENET_PLL               0x1201UL
#define IMX_CCM_ENET1G_CLK             0x1202UL
#define IMX_CCM_ENET1G_PLL             0x1203UL

/* FLEXSPI */
#define IMX_CCM_FLEXSPI_CLK            0x1300UL
#define IMX_CCM_FLEXSPI2_CLK           0x1301UL

/* PIT */
#define IMX_CCM_PIT_CLK                0x1400UL
#define IMX_CCM_PIT1_CLK               0x1401UL

/* ADC */
#define IMX_CCM_LPADC1_CLK             0x1500UL
#define IMX_CCM_LPADC2_CLK             0x1501UL
#define IMX_CCM_SAR_ADC1_CLK           0x1500UL

/* TPM */
#define IMX_CCM_TPM_CLK                0x1600UL
#define IMX_CCM_TPM1_CLK               0x1600UL
#define IMX_CCM_TPM2_CLK               0x1601UL
#define IMX_CCM_TPM3_CLK               0x1602UL
#define IMX_CCM_TPM4_CLK               0x1603UL
#define IMX_CCM_TPM5_CLK               0x1604UL
#define IMX_CCM_TPM6_CLK               0x1605UL

/* FLEXIO */
#define IMX_CCM_FLEXIO_CLK             0x1700UL
#define IMX_CCM_FLEXIO1_CLK            0x1700UL
#define IMX_CCM_FLEXIO2_CLK            0x1701UL

/* NETC */
#define IMX_CCM_NETC_CLK 0x1800UL

/* MIPI CSI2RX */
#define IMX_CCM_MIPI_CSI2RX_ROOT_CLK 0x1900UL
#define IMX_CCM_MIPI_CSI2RX_UI_CLK   0x2000UL
#define IMX_CCM_MIPI_CSI2RX_ESC_CLK  0x2100UL

/* I3C */
#define IMX_CCM_I3C_CLK                0x2200UL
#define IMX_CCM_I3C1_CLK               0x2200UL
#define IMX_CCM_I3C2_CLK               0x2201UL

/* LPIT */
#define IMX_CCM_LPIT_CLK  0x2300UL
#define IMX_CCM_LPIT1_CLK 0x2300UL
#define IMX_CCM_LPIT2_CLK 0x2301UL
#define IMX_CCM_LPIT3_CLK 0x2302UL

/* KPP */
#define IMX_CCM_KPP_CLK                0x2400UL

/* USB */
#define IMX_CCM_USB_CLK                0x2500UL
#define IMX_CCM_USB_PHY_CLK            0x2600UL

#define IMX_CCM_SYSCTR_BASE_CLK        0x2700UL
#define IMX_CCM_SYSCTR_SLOW_CLK        0x2701UL

#define IMX_CCM_PDM_CLK                0x2800UL

/* XBAR */
#define IMX_CCM_XBAR1_CLK             0x2900UL
#define IMX_CCM_XBAR2_CLK             0x2901UL
#define IMX_CCM_XBAR3_CLK             0x2902UL

/* ENC (EQDC) */
#define IMX_CCM_ENC1_CLK               0x2A00UL
#define IMX_CCM_ENC2_CLK               0x2A01UL
#define IMX_CCM_ENC3_CLK               0x2A02UL
#define IMX_CCM_ENC4_CLK               0x2A03UL

/* QTMR */
#define IMX_CCM_QTMR_CLK               0x6000UL
#define IMX_CCM_QTMR1_CLK              0x6000UL
#define IMX_CCM_QTMR2_CLK              0x6001UL
#define IMX_CCM_QTMR3_CLK              0x6002UL
#define IMX_CCM_QTMR4_CLK              0x6003UL

/* MEDIA */
#define IMX_CCM_MEDIA_AXI_CLK      0x3000UL
#define IMX_CCM_MEDIA_APB_CLK      0x3100UL
#define IMX_CCM_MEDIA_DISP_PIX_CLK 0x3200UL
#define IMX_CCM_MEDIA_LDB_CLK      0x3300UL
#define IMX_CCM_MIPI_PHY_CFG_CLK   0x3400UL
#define IMX_CCM_CAM_PIX_CLK        0x3500UL

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV2_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2021,2024-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

外设（Peripheral）：范围 `0–0xFF`，从 0 开始编号。

实例（Instance）：范围 `0–0xFF`，从 0 开始编号。

### 注释 3：原第 23 行

由 `ARM_PLL` 驱动的 Cortex-A55 内核时钟（Core Clock）。

### 注释 4：原第 26 行

低功耗通用异步收发器（LPUART）。

### 注释 5：原第 47 行

低功耗集成电路间总线（LPI2C）。

### 注释 6：原第 62 行

低功耗串行外设接口（LPSPI）。

### 注释 7：原第 76 行

超高速 SD 主机控制器（USDHC）。

### 注释 8：原第 82 行

直接内存访问（DMA）

### 注释 9：原第 88 行

脉宽调制（PWM）

### 注释 10：原第 91 行

控制器局域网（CAN）

### 注释 11：原第 97 行

通用定时器（GPT）。

### 注释 12：原第 106 行

同步音频接口（SAI）。

### 注释 13：原第 112 行

以太网（ENET）。

### 注释 14：原第 118 行

FlexSPI 串行外设接口（FLEXSPI）。

### 注释 15：原第 122 行

周期中断定时器（PIT）。

### 注释 16：原第 126 行

模数转换器（ADC）

### 注释 17：原第 131 行

定时器／PWM 模块（TPM）。

### 注释 18：原第 140 行

灵活输入输出模块（FLEXIO）。

### 注释 19：原第 145 行

网络控制器（NETC）。

### 注释 20：原第 148 行

MIPI 相机串行接口 2 接收器（CSI2RX）。

### 注释 21：原第 153 行

改进型集成电路间总线（I3C）

### 注释 22：原第 158 行

低功耗中断定时器（LPIT）。

### 注释 23：原第 164 行

键盘端口（KPP）。

### 注释 24：原第 167 行

通用串行总线（USB）

### 注释 25：原第 179 行

交叉开关（XBAR）。

### 注释 26：原第 187 行

编码器（ENC），即增强型正交解码器（EQDC）。

### 注释 27：原第 197 行

四通道定时器（QTMR）。

### 注释 28：原第 204 行

媒体模块（MEDIA）。

### 注释 29：原第 212 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV2_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h.html)

---

[上一章](P003_ethernet.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_intc_vim.h_源码浏览.md)
