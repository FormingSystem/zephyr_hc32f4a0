---
id: learning.zephyr-docs.api-file-display-chat-reference.page-21
title: zephyr__dt-bindings__reset__syna_sr100_reset.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_dt-bindings\_\_reset\_\_syna\_sr100\_reset.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出Synaptics SR100系列的复位子系统ID（Reset Subsystem IDs）。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

列出Synaptics SR100系列的复位子系统ID（Reset Subsystem IDs）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_aec7d4fd434ace789a90c73f48ce15988"></a>

```c
#define IMGPROC_RST 0x20
```

相关声明：[IMGPROC_RST](#aec7d4fd434ace789a90c73f48ce15988)。

用于 RST_REG 值的辅助宏（Helpers）。

<a id="r_a7508ae4bc67c2db30114a0f0f1a7131d"></a>

```c
#define NPU_RST 0x30
```

相关声明：[NPU_RST](#a7508ae4bc67c2db30114a0f0f1a7131d)。

NPU 复位（Reset）。

<a id="r_ab6eedee4ccab7334b7d63971ca9aef95"></a>

```c
#define DMA0_RST 0x40
```

相关声明：[DMA0_RST](#ab6eedee4ccab7334b7d63971ca9aef95)。

DMA0 复位（Reset）。

<a id="r_ad9f78022a0b051f78590d3214e331d59"></a>

```c
#define DMA1_RST 0x48
```

相关声明：[DMA1_RST](#ad9f78022a0b051f78590d3214e331d59)。

DMA1 复位（Reset）。

<a id="r_aa44f3af330694a436bc8e135e5886593"></a>

```c
#define AXI_RST 0x50
```

相关声明：[AXI_RST](#aa44f3af330694a436bc8e135e5886593)。

AXI 复位（Reset）。

<a id="r_a2c57ea866e88e54dc1aa351ae661487b"></a>

```c
#define APB_PERIF_RST 0x8C
```

相关声明：[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)。

APB 复位字段辅助宏（Reset Field Helper）。

<a id="r_a1a8f2b9f47ad4b01554f1ad25dceddbc"></a>

```c
#define PERIF_RST 0x80
```

相关声明：[PERIF_RST](#a1a8f2b9f47ad4b01554f1ad25dceddbc)。

外设复位字段辅助宏（Reset Field Helper）。

<a id="r_a153802262e3a1cb5adba894cdb402e12"></a>

```c
#define TOP_STICKY_RST 0x58
```

相关声明：[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)。

用于 STI_REG 值的辅助宏（Helpers）。

<a id="r_a42fd7f8d1487c9fab7782bfe6af21a67"></a>

```c
#define PER_STICKY_RST 0x88
```

相关声明：[PER_STICKY_RST](#a42fd7f8d1487c9fab7782bfe6af21a67)。

USB 粘滞字段辅助宏（Sticky Field Helper）。

<a id="r_ad11217492cdebe1933460b0e3224c343"></a>

```c
#define STI_REG 24
```

相关声明：[STI_REG](#ad11217492cdebe1933460b0e3224c343)。

寄存器字段辅助宏（Register Field Helpers）。

<a id="r_a06983db01859b4142249016d8df4cd1d"></a>

```c
#define STI_MASK 21
```

相关声明：[STI_MASK](#a06983db01859b4142249016d8df4cd1d)。

粘滞字段位掩码（Sticky Field Bit Mask）。

<a id="r_a113c86edabe2eb9e8e3c7078ae18b69f"></a>

```c
#define STI_BIT 16
```

相关声明：[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)。

粘滞位（Sticky Bit）。

<a id="r_ad011f59e3a8c7100ea437bd90a664b07"></a>

```c
#define RST_REG 8
```

相关声明：[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)。

复位字段位移量（Reset Field Bit Shift）。

<a id="r_ab58c156fb4ee981a9d5ad151ab528351"></a>

```c
#define RST_MASK 5
```

相关声明：[RST_MASK](#ab58c156fb4ee981a9d5ad151ab528351)。

复位字段位掩码（Reset Field Bit Mask）。

<a id="r_a4fd25080f68af502175597fcdd684b11"></a>

```c
#define RST_BIT 0
```

相关声明：[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

复位位位移量（Reset Bit Shift）。

<a id="r_a88ec219217d8ca466e428b9663f3721b"></a>

```c
#define SYNA_IMGPRC_RST ((TOP_STICKY_RST << STI_REG) | (1 << STI_BIT) | (IMGPROC_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_IMGPRC_RST](#a88ec219217d8ca466e428b9663f3721b)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)、[IMGPROC_RST](#aec7d4fd434ace789a90c73f48ce15988)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

设备域复位选择（Device Domain Reset Selection）。

<a id="r_ad85961f7dea187c06f1f610f1499da83"></a>

```c
#define SYNA_NPU_RST ((TOP_STICKY_RST << STI_REG) | (0 << STI_BIT) | (NPU_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_NPU_RST](#ad85961f7dea187c06f1f610f1499da83)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)、[NPU_RST](#a7508ae4bc67c2db30114a0f0f1a7131d)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

NPU 复位（Reset）。

<a id="r_ae3f54ab1576cda5b9310bcd62833c769"></a>

```c
#define SYNA_DMA0_RST ((TOP_STICKY_RST << STI_REG) | (2 << STI_BIT) | (DMA0_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_DMA0_RST](#ae3f54ab1576cda5b9310bcd62833c769)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)、[DMA0_RST](#ab6eedee4ccab7334b7d63971ca9aef95)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

DMA0 复位（Reset）。

<a id="r_a5ffe09e7fbf09495095a7fa5f6678269"></a>

```c
#define SYNA_DMA1_RST ((TOP_STICKY_RST << STI_REG) | (5 << STI_BIT) | (DMA1_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_DMA1_RST](#a5ffe09e7fbf09495095a7fa5f6678269)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)、[DMA1_RST](#ad9f78022a0b051f78590d3214e331d59)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

DMA1 复位（Reset）。

<a id="r_af683862620dda69823558284484b6d24"></a>

```c
#define SYNA_AXI_RST ((AXI_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_AXI_RST](#af683862620dda69823558284484b6d24)、[AXI_RST](#aa44f3af330694a436bc8e135e5886593)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

AXI 复位（Reset）。

<a id="r_ac40371ce6aca98040c6a8e5ba5961523"></a>

```c
#define SYNA_OTP_RST ((TOP_STICKY_RST << STI_REG) | (3 << STI_BIT))
```

相关声明：[SYNA_OTP_RST](#ac40371ce6aca98040c6a8e5ba5961523)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)。

OTP 复位（Reset）。

<a id="r_a7a0c44a7a47fc2ff57348221d46f10f4"></a>

```c
#define SYNA_CALIB_RST ((TOP_STICKY_RST << STI_REG) | (6 << STI_BIT))
```

相关声明：[SYNA_CALIB_RST](#a7a0c44a7a47fc2ff57348221d46f10f4)、[TOP_STICKY_RST](#a153802262e3a1cb5adba894cdb402e12)、[STI_REG](#ad11217492cdebe1933460b0e3224c343)、[STI_BIT](#a113c86edabe2eb9e8e3c7078ae18b69f)。

时钟校准复位（Clock Calibration Reset）。

<a id="r_a7b94d2ffe453d2df8f8b3a1fa1bda048"></a>

```c
#define SYNA_USB_RST
```

相关声明：[SYNA_USB_RST](#a7b94d2ffe453d2df8f8b3a1fa1bda048)。

USB 复位（Reset）。

<a id="r_afe5ab31a5a99df63baeed1aa3913911d"></a>

```c
#define SYNA_UART0_RST ((APB_PERIF_RST << RST_REG) | (0 << RST_BIT))
```

相关声明：[SYNA_UART0_RST](#afe5ab31a5a99df63baeed1aa3913911d)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

UART0 复位（Reset）。

<a id="r_aa355e17b90687eaafcc3ddf5eb2dde24"></a>

```c
#define SYNA_UART1_RST ((APB_PERIF_RST << RST_REG) | (1 << RST_BIT))
```

相关声明：[SYNA_UART1_RST](#aa355e17b90687eaafcc3ddf5eb2dde24)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

UART1 复位（Reset）。

<a id="r_a1182c07950676c456787fffa4f84251d"></a>

```c
#define SYNA_I2C0M_RST ((APB_PERIF_RST << RST_REG) | (2 << RST_BIT))
```

相关声明：[SYNA_I2C0M_RST](#a1182c07950676c456787fffa4f84251d)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

I2C0 主设备复位（Master Reset）。

<a id="r_aab26e8683444b6ecaf42c7baee390a34"></a>

```c
#define SYNA_I2C1M_RST ((APB_PERIF_RST << RST_REG) | (3 << RST_BIT))
```

相关声明：[SYNA_I2C1M_RST](#aab26e8683444b6ecaf42c7baee390a34)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

I2C1 主设备复位（Master Reset）。

<a id="r_ab5f265de883ae33cf2e58840c6112268"></a>

```c
#define SYNA_I2CS_RST ((APB_PERIF_RST << RST_REG) | (4 << RST_BIT))
```

相关声明：[SYNA_I2CS_RST](#ab5f265de883ae33cf2e58840c6112268)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

I2C 从设备复位（Slave Reset）。

<a id="r_af8271d07e8af6e96bfc647deec2a99a5"></a>

```c
#define SYNA_I3C0_RST ((APB_PERIF_RST << RST_REG) | (5 << RST_BIT))
```

相关声明：[SYNA_I3C0_RST](#af8271d07e8af6e96bfc647deec2a99a5)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

I3C0 复位（Reset）。

<a id="r_aa1127b468b329994635f4d8a07178583"></a>

```c
#define SYNA_I3C1_RST ((APB_PERIF_RST << RST_REG) | (6 << RST_BIT))
```

相关声明：[SYNA_I3C1_RST](#aa1127b468b329994635f4d8a07178583)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

I3C1 复位（Reset）。

<a id="r_a1ba07da1324ef88bf49577af1801ceee"></a>

```c
#define SYNA_SPIM_RST ((APB_PERIF_RST << RST_REG) | (7 << RST_BIT))
```

相关声明：[SYNA_SPIM_RST](#a1ba07da1324ef88bf49577af1801ceee)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

SPI 主设备复位（Master Reset）。

<a id="r_a120aec61004c30b23877707c1d721b5a"></a>

```c
#define SYNA_SPIS_RST ((APB_PERIF_RST << RST_REG) | (8 << RST_BIT))
```

相关声明：[SYNA_SPIS_RST](#a120aec61004c30b23877707c1d721b5a)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

SPI 从设备复位（Slave Reset）。

<a id="r_aaab37925f3d8fba544066d253c2076ac"></a>

```c
#define SYNA_GPIO_RST ((APB_PERIF_RST << RST_REG) | (9 << RST_BIT))
```

相关声明：[SYNA_GPIO_RST](#aaab37925f3d8fba544066d253c2076ac)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

GPIO 复位（Reset）。

<a id="r_a3268df23e588d91b21adc217359a84d0"></a>

```c
#define SYNA_SWIRE_RST ((APB_PERIF_RST << RST_REG) | (19 << RST_BIT))
```

相关声明：[SYNA_SWIRE_RST](#a3268df23e588d91b21adc217359a84d0)、[APB_PERIF_RST](#a2c57ea866e88e54dc1aa351ae661487b)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

Soundwire 复位（Reset）。

<a id="r_a9ebf2cdf039d21295959c1529588eac7"></a>

```c
#define SYNA_SD0_RST ((PERIF_RST << RST_REG) | (2 << RST_BIT))
```

相关声明：[SYNA_SD0_RST](#a9ebf2cdf039d21295959c1529588eac7)、[PERIF_RST](#a1a8f2b9f47ad4b01554f1ad25dceddbc)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

SD0 复位（Reset）。

<a id="r_a21942a8979341930876144f6d8fb4537"></a>

```c
#define SYNA_SD1_RST ((PERIF_RST << RST_REG) | (3 << RST_BIT))
```

相关声明：[SYNA_SD1_RST](#a21942a8979341930876144f6d8fb4537)、[PERIF_RST](#a1a8f2b9f47ad4b01554f1ad25dceddbc)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

SD1 复位（Reset）。

<a id="r_ae0754392c581716fd3958f3f33113e1e"></a>

```c
#define SYNA_XSPI_RST ((PERIF_RST << RST_REG) | (5 << RST_BIT))
```

相关声明：[SYNA_XSPI_RST](#ae0754392c581716fd3958f3f33113e1e)、[PERIF_RST](#a1a8f2b9f47ad4b01554f1ad25dceddbc)、[RST_REG](#ad011f59e3a8c7100ea437bd90a664b07)、[RST_BIT](#a4fd25080f68af502175597fcdd684b11)。

xSPI 复位（Reset）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a2c57ea866e88e54dc1aa351ae661487b"></a>

### `APB_PERIF_RST`

```c
#define APB_PERIF_RST 0x8C
```

APB 复位字段辅助宏（Reset Field Helper）。

<a id="aa44f3af330694a436bc8e135e5886593"></a>

### `AXI_RST`

```c
#define AXI_RST 0x50
```

AXI 复位（Reset）。

<a id="ab6eedee4ccab7334b7d63971ca9aef95"></a>

### `DMA0_RST`

```c
#define DMA0_RST 0x40
```

DMA0 复位（Reset）。

<a id="ad9f78022a0b051f78590d3214e331d59"></a>

### `DMA1_RST`

```c
#define DMA1_RST 0x48
```

DMA1 复位（Reset）。

<a id="aec7d4fd434ace789a90c73f48ce15988"></a>

### `IMGPROC_RST`

```c
#define IMGPROC_RST 0x20
```

用于 RST_REG 值的辅助宏（Helpers）。

图像处理复位（Image Processing Reset）。

<a id="a7508ae4bc67c2db30114a0f0f1a7131d"></a>

### `NPU_RST`

```c
#define NPU_RST 0x30
```

NPU 复位（Reset）。

<a id="a42fd7f8d1487c9fab7782bfe6af21a67"></a>

### `PER_STICKY_RST`

```c
#define PER_STICKY_RST 0x88
```

USB 粘滞字段辅助宏（Sticky Field Helper）。

<a id="a1a8f2b9f47ad4b01554f1ad25dceddbc"></a>

### `PERIF_RST`

```c
#define PERIF_RST 0x80
```

外设复位字段辅助宏（Reset Field Helper）。

<a id="a4fd25080f68af502175597fcdd684b11"></a>

### `RST_BIT`

```c
#define RST_BIT 0
```

复位位位移量（Reset Bit Shift）。

<a id="ab58c156fb4ee981a9d5ad151ab528351"></a>

### `RST_MASK`

```c
#define RST_MASK 5
```

复位字段位掩码（Reset Field Bit Mask）。

<a id="ad011f59e3a8c7100ea437bd90a664b07"></a>

### `RST_REG`

```c
#define RST_REG 8
```

复位字段位移量（Reset Field Bit Shift）。

<a id="a113c86edabe2eb9e8e3c7078ae18b69f"></a>

### `STI_BIT`

```c
#define STI_BIT 16
```

粘滞位（Sticky Bit）。

<a id="a06983db01859b4142249016d8df4cd1d"></a>

### `STI_MASK`

```c
#define STI_MASK 21
```

粘滞字段位掩码（Sticky Field Bit Mask）。

<a id="ad11217492cdebe1933460b0e3224c343"></a>

### `STI_REG`

```c
#define STI_REG 24
```

寄存器字段辅助宏（Register Field Helpers）。

粘滞字段位移量（Sticky Field Bit Shift）。

<a id="af683862620dda69823558284484b6d24"></a>

### `SYNA_AXI_RST`

```c
#define SYNA_AXI_RST ((AXI_RST << RST_REG) | (0 << RST_BIT))
```

AXI 复位（Reset）。

<a id="a7a0c44a7a47fc2ff57348221d46f10f4"></a>

### `SYNA_CALIB_RST`

```c
#define SYNA_CALIB_RST ((TOP_STICKY_RST << STI_REG) | (6 << STI_BIT))
```

时钟校准复位（Clock Calibration Reset）。

<a id="ae3f54ab1576cda5b9310bcd62833c769"></a>

### `SYNA_DMA0_RST`

```c
#define SYNA_DMA0_RST ((TOP_STICKY_RST << STI_REG) | (2 << STI_BIT) | (DMA0_RST << RST_REG) | (0 << RST_BIT))
```

DMA0 复位（Reset）。

<a id="a5ffe09e7fbf09495095a7fa5f6678269"></a>

### `SYNA_DMA1_RST`

```c
#define SYNA_DMA1_RST ((TOP_STICKY_RST << STI_REG) | (5 << STI_BIT) | (DMA1_RST << RST_REG) | (0 << RST_BIT))
```

DMA1 复位（Reset）。

<a id="aaab37925f3d8fba544066d253c2076ac"></a>

### `SYNA_GPIO_RST`

```c
#define SYNA_GPIO_RST ((APB_PERIF_RST << RST_REG) | (9 << RST_BIT))
```

GPIO 复位（Reset）。

<a id="a1182c07950676c456787fffa4f84251d"></a>

### `SYNA_I2C0M_RST`

```c
#define SYNA_I2C0M_RST ((APB_PERIF_RST << RST_REG) | (2 << RST_BIT))
```

I2C0 主设备复位（Master Reset）。

<a id="aab26e8683444b6ecaf42c7baee390a34"></a>

### `SYNA_I2C1M_RST`

```c
#define SYNA_I2C1M_RST ((APB_PERIF_RST << RST_REG) | (3 << RST_BIT))
```

I2C1 主设备复位（Master Reset）。

<a id="ab5f265de883ae33cf2e58840c6112268"></a>

### `SYNA_I2CS_RST`

```c
#define SYNA_I2CS_RST ((APB_PERIF_RST << RST_REG) | (4 << RST_BIT))
```

I2C 从设备复位（Slave Reset）。

<a id="af8271d07e8af6e96bfc647deec2a99a5"></a>

### `SYNA_I3C0_RST`

```c
#define SYNA_I3C0_RST ((APB_PERIF_RST << RST_REG) | (5 << RST_BIT))
```

I3C0 复位（Reset）。

<a id="aa1127b468b329994635f4d8a07178583"></a>

### `SYNA_I3C1_RST`

```c
#define SYNA_I3C1_RST ((APB_PERIF_RST << RST_REG) | (6 << RST_BIT))
```

I3C1 复位（Reset）。

<a id="a88ec219217d8ca466e428b9663f3721b"></a>

### `SYNA_IMGPRC_RST`

```c
#define SYNA_IMGPRC_RST ((TOP_STICKY_RST << STI_REG) | (1 << STI_BIT) | (IMGPROC_RST << RST_REG) | (0 << RST_BIT))
```

设备域复位选择（Device Domain Reset Selection）。

图像处理复位（Image Processing Reset）。

<a id="ad85961f7dea187c06f1f610f1499da83"></a>

### `SYNA_NPU_RST`

```c
#define SYNA_NPU_RST ((TOP_STICKY_RST << STI_REG) | (0 << STI_BIT) | (NPU_RST << RST_REG) | (0 << RST_BIT))
```

NPU 复位（Reset）。

<a id="ac40371ce6aca98040c6a8e5ba5961523"></a>

### `SYNA_OTP_RST`

```c
#define SYNA_OTP_RST ((TOP_STICKY_RST << STI_REG) | (3 << STI_BIT))
```

OTP 复位（Reset）。

<a id="a9ebf2cdf039d21295959c1529588eac7"></a>

### `SYNA_SD0_RST`

```c
#define SYNA_SD0_RST ((PERIF_RST << RST_REG) | (2 << RST_BIT))
```

SD0 复位（Reset）。

<a id="a21942a8979341930876144f6d8fb4537"></a>

### `SYNA_SD1_RST`

```c
#define SYNA_SD1_RST ((PERIF_RST << RST_REG) | (3 << RST_BIT))
```

SD1 复位（Reset）。

<a id="a1ba07da1324ef88bf49577af1801ceee"></a>

### `SYNA_SPIM_RST`

```c
#define SYNA_SPIM_RST ((APB_PERIF_RST << RST_REG) | (7 << RST_BIT))
```

SPI 主设备复位（Master Reset）。

<a id="a120aec61004c30b23877707c1d721b5a"></a>

### `SYNA_SPIS_RST`

```c
#define SYNA_SPIS_RST ((APB_PERIF_RST << RST_REG) | (8 << RST_BIT))
```

SPI 从设备复位（Slave Reset）。

<a id="a3268df23e588d91b21adc217359a84d0"></a>

### `SYNA_SWIRE_RST`

```c
#define SYNA_SWIRE_RST ((APB_PERIF_RST << RST_REG) | (19 << RST_BIT))
```

Soundwire 复位（Reset）。

<a id="afe5ab31a5a99df63baeed1aa3913911d"></a>

### `SYNA_UART0_RST`

```c
#define SYNA_UART0_RST ((APB_PERIF_RST << RST_REG) | (0 << RST_BIT))
```

UART0 复位（Reset）。

<a id="aa355e17b90687eaafcc3ddf5eb2dde24"></a>

### `SYNA_UART1_RST`

```c
#define SYNA_UART1_RST ((APB_PERIF_RST << RST_REG) | (1 << RST_BIT))
```

UART1 复位（Reset）。

<a id="a7b94d2ffe453d2df8f8b3a1fa1bda048"></a>

### `SYNA_USB_RST`

```c
#define SYNA_USB_RST
```

展开值（Value）：

```c
((PER_STICKY_RST << STI_REG) | (0 << STI_BIT) | (7 << STI_MASK) | (PERIF_RST << RST_REG) | \
 (4 << RST_BIT))
```

USB 复位（Reset）。

<a id="ae0754392c581716fd3958f3f33113e1e"></a>

### `SYNA_XSPI_RST`

```c
#define SYNA_XSPI_RST ((PERIF_RST << RST_REG) | (5 << RST_BIT))
```

xSPI 复位（Reset）。

<a id="a153802262e3a1cb5adba894cdb402e12"></a>

### `TOP_STICKY_RST`

```c
#define TOP_STICKY_RST 0x58
```

用于 STI_REG 值的辅助宏（Helpers）。

外设粘滞字段辅助宏（Sticky Field Helper）。


## 21.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P850_syna_sr100_reset.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asyna__sr100__reset_8h_html_a06983db01859b4142249016d8df4cd1d"></a>
<a id="asyna__sr100__reset_8h_html_a113c86edabe2eb9e8e3c7078ae18b69f"></a>
<a id="asyna__sr100__reset_8h_html_a1a8f2b9f47ad4b01554f1ad25dceddbc"></a>
<a id="asyna__sr100__reset_8h_html_a42fd7f8d1487c9fab7782bfe6af21a67"></a>
<a id="asyna__sr100__reset_8h_html_a4fd25080f68af502175597fcdd684b11"></a>
<a id="asyna__sr100__reset_8h_html_ad011f59e3a8c7100ea437bd90a664b07"></a>
<a id="asyna__sr100__reset_8h_html_ad11217492cdebe1933460b0e3224c343"></a>

---

[上一章](P020_____w__zephyr__zephyr__modules__openthread__include__openthread.h_文件参考.md) · [返回大纲](大纲.md)
