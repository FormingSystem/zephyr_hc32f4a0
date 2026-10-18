---
id: learning.zephyr-docs.boards-shields.page-45
title: ArduCam Mega SPI Camera Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arducam_mega/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arducam-mega-spi-camera-shield"></a>

<a id="arducam-mega"></a>

# 第45章\_ArduCam Mega SPI摄像头扩展板（Camera Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arducam_mega/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

ArduCam Mega SPI扩展板通过标准SPI接口提供Arducam Mega图像传感器，共有4个变体：


- arducam_mega：通用变体，需要板级覆盖文件
- arducam_mega_arduino：用于提供Arduino兼容SPI排针的开发板
- arducam_mega_mikrobus：用于提供mikroBUS连接器的开发板
- arducam_mega_xiao：用于提供Seeed XIAO连接器的开发板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板要求开发板提供：


- 一条SPI总线
- 一个片选GPIO

各连接器专用变体依赖开发板的标准SPI别名arduino_spi、mikrobus_spi或xiao_spi，并将其赋给共用arducam_mega.overlay使用的arducam_mega_spi别名。基础arducam_mega变体需要板级覆盖文件，手工定义该别名及片选引脚。

<a id="board-overlays"></a>

### 开发板覆盖文件（Board Overlays）

连接器专用变体将相应SPI总线赋给arducam_mega_spi，再包含共用arducam_mega.overlay，由后者注册设备节点并设置zephyr,camera。

arducam_mega_arduino使用arduino_spi别名：

```text
arducam_mega_spi: &arduino_spi {};
#include "arducam_mega.overlay"
```

arducam_mega_mikrobus使用mikrobus_spi别名：

```text
arducam_mega_spi: &mikrobus_spi {};
#include "arducam_mega.overlay"
```

arducam_mega_xiao使用xiao_spi别名：

```text
arducam_mega_spi: &xiao_spi {};
#include "arducam_mega.overlay"
```

arducam_mega为通用变体，其扩展板覆盖文件有意留空。在扩展板目录创建boards/<board_name>.overlay，并将<board_spi_bus>、<gpio_port>及<pin>替换为实际板卡值：

```text
arducam_mega_spi: &<board_spi_bus> {
    cs-gpios = <&<gpio_port> <pin> GPIO_ACTIVE_LOW>;
};
#include "arducam_mega.overlay"
```

所有变体包含的共用arducam_mega.overlay内容如下：

```text
/ {
    chosen {
        zephyr,camera = &arducam_mega;
    };
};

&arducam_mega_spi {
    arducam_mega: arducam-mega@0 {
        compatible = "arducam,mega";
        reg = <0>;
        spi-max-frequency = <4000000>;
    };
};
```

<a id="programming"></a>

## 编程（Programming）

选择与开发板连接器匹配的变体并传给west build。例如，在nucleo_h563zi上使用Arduino变体：

```text
# From the root of the zephyr repository
west build -b nucleo_h563zi --shield arducam_mega_arduino samples/subsys/video/tcpserversink -- -DCONFIG_NET_PKT_RX_COUNT=10 -DCONFIG_NET_PKT_TX_COUNT=10 -DCONFIG_NET_BUF_RX_COUNT=20 -DCONFIG_NET_BUF_TX_COUNT=20 -DCONFIG_NET_MAX_CONTEXTS=10 -DCONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE=131072 -DCONFIG_VIDEO_FRAME_WIDTH=96 -DCONFIG_VIDEO_FRAME_HEIGHT=96 -DCONFIG_VIDEO_PIXEL_FORMAT=\"JPEG\"
west flash
```

<a id="references"></a>

## 参考资料（References）

---

[上一章](P044_ArduCam_CU450_OV5640_Camera_Module.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P046_Arduino_GIGA_Display_Shield.md)
