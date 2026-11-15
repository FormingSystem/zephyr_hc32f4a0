---
id: learning.zephyr-docs.dt-peripheral-reference.page-1
title: GPIO设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_GPIO设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2gpio_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择GPIO、SPI、CAN或显示设备树头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

通用输入输出（GPIO）设备树宏公共 API 头文件。

查看此文件的源码。

<a id="details"></a>

通用输入输出（GPIO）设备树宏公共 API 头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga97bd46d2ab88d392a3f336f4d23184eb"></a>

```c
#define DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, idx)
```

相关声明：[DT_GPIO_CTLR_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga97bd46d2ab88d392a3f336f4d23184eb)。

从 GPIO 句柄数组（Phandle Array）属性的指定索引处取得控制器句柄对应的节点标识符。

<a id="r_gafbad7d0d7f7fb9338997482c8da0e566"></a>

```c
#define DT_GPIO_CTLR(node_id, gpio_pha)
```

相关声明：[DT_GPIO_CTLR](../hardware/P290_设备树GPIO宏.md#gafbad7d0d7f7fb9338997482c8da0e566)。

等价于 `DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, 0)`。

<a id="r_ga8f7d82567056266bab1603865f8b27af"></a>

```c
#define DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, idx)
```

相关声明：[DT_GPIO_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga8f7d82567056266bab1603865f8b27af)。

取得指定索引处 GPIO 描述符（Specifier）的 pin 单元。

<a id="r_ga4e41ec30ece058555333811a9fcee333"></a>

```c
#define DT_GPIO_PIN(node_id, gpio_pha)
```

相关声明：[DT_GPIO_PIN](../hardware/P290_设备树GPIO宏.md#ga4e41ec30ece058555333811a9fcee333)。

等价于 `DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, 0)`。

<a id="r_ga672b2597b99194b8cbd42b3f3401d2b5"></a>

```c
#define DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, idx)
```

相关声明：[DT_GPIO_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga672b2597b99194b8cbd42b3f3401d2b5)。

取得指定索引处 GPIO 描述符的 flags 单元。

<a id="r_ga32b3383d7ed543602a7b4a031018316f"></a>

```c
#define DT_GPIO_FLAGS(node_id, gpio_pha)
```

相关声明：[DT_GPIO_FLAGS](../hardware/P290_设备树GPIO宏.md#ga32b3383d7ed543602a7b4a031018316f)。

等价于 `DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, 0)`。

<a id="r_ga0a4575c3750db76692fd0f817a169b50"></a>

```c
#define DT_NUM_GPIO_HOGS(node_id)
```

相关声明：[DT_NUM_GPIO_HOGS](../hardware/P290_设备树GPIO宏.md#ga0a4575c3750db76692fd0f817a169b50)。

取得节点中 GPIO 预占项（GPIO Hogs）的数量。

<a id="r_gaf4ecdebbd433473f654f4b6859542af9"></a>

```c
#define DT_GPIO_HOG_PIN_BY_IDX(node_id, idx)
```

相关声明：[DT_GPIO_HOG_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#gaf4ecdebbd433473f654f4b6859542af9)。

取得指定索引处 GPIO 预占描述符的 pin 单元。

<a id="r_gaed024e6acac49f591fe50cd43e8af14f"></a>

```c
#define DT_GPIO_HOG_FLAGS_BY_IDX(node_id, idx)
```

相关声明：[DT_GPIO_HOG_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#gaed024e6acac49f591fe50cd43e8af14f)。

取得指定索引处 GPIO 预占描述符的 flags 单元。

<a id="r_ga162bca126f7015816286358f09bde6ff"></a>

```c
#define DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, idx)
```

相关声明：[DT_INST_GPIO_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga162bca126f7015816286358f09bde6ff)。

取得 DT_DRV_COMPAT 实例在指定索引处 GPIO 描述符的 pin 单元值。

<a id="r_ga5ee13b3de1d4cecc877963dfa8820cfd"></a>

```c
#define DT_INST_GPIO_PIN(inst, gpio_pha)
```

相关声明：[DT_INST_GPIO_PIN](../hardware/P290_设备树GPIO宏.md#ga5ee13b3de1d4cecc877963dfa8820cfd)。

等价于 `DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, 0)`。

<a id="r_gafd40d1eec5c1672b7675ae47388c1cef"></a>

```c
#define DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, idx)
```

相关声明：[DT_INST_GPIO_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#gafd40d1eec5c1672b7675ae47388c1cef)。

取得 DT_DRV_COMPAT 实例在指定索引处 GPIO 描述符的 flags 单元。

<a id="r_ga8d3edd53d6d8e89afc68f0c10176f57f"></a>

```c
#define DT_INST_GPIO_FLAGS(inst, gpio_pha)
```

相关声明：[DT_INST_GPIO_FLAGS](../hardware/P290_设备树GPIO宏.md#ga8d3edd53d6d8e89afc68f0c10176f57f)。

等价于 `DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, 0)`。

## 1.2\_源码定位与版本边界

相对源码定位：[GPIO宏](../../../include/zephyr/devicetree/gpio.h)、[SPI宏](../../../include/zephyr/devicetree/spi.h)、[CAN宏](../../../include/zephyr/devicetree/can.h)、[显示宏](../../../include/zephyr/devicetree/display.h)、[宏生成器](../../../scripts/dts/gen_defines.py)和[显示列表绑定](../../../dts/bindings/display/zephyr,displays.yaml)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：三种返回对象：CTLR系列返回GPIO控制器节点标识，PIN读取绑定中名为pin的单元，FLAGS读取名为flags的单元，缺少该单元时回退为0。节点标识不是struct device指针，引脚编号也不是电平读数；flags为0不证明条目有效、控制器就绪或引脚已配置。

> 译注——源码核对：预占项属于hog节点：DT_NUM_GPIO_HOGS读取传入节点的_GPIO_HOGS元数据，统计该gpio-hog节点中预占GPIO描述符的数量，不是其父GPIO控制器拥有的所有hog子节点数量。没有元数据时数量为0，PIN_BY_IDX没有同样的零值回退；访问前仍需使用有效索引。gen_defines.py逐项遍历node.gpio_hogs生成这些值。

> 译注——源码核对：实例与默认索引：INST接口通过DT_DRV_INST(inst)取得消费节点，再读取该节点的GPIO属性；它不把inst当成GPIO控制器编号。省略BY_IDX的版本固定选择索引0。这些宏读取编译期描述，不调用gpio_pin_configure，也不完成GPIO hog初始化。

> 译注——源码核对：版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P002_GPIO设备树头文件源码.md)
- [DT_GPIO_CTLR_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga97bd46d2ab88d392a3f336f4d23184eb)
- [DT_GPIO_CTLR](../hardware/P290_设备树GPIO宏.md#gafbad7d0d7f7fb9338997482c8da0e566)
- [DT_GPIO_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga8f7d82567056266bab1603865f8b27af)
- [DT_GPIO_PIN](../hardware/P290_设备树GPIO宏.md#ga4e41ec30ece058555333811a9fcee333)
- [DT_GPIO_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga672b2597b99194b8cbd42b3f3401d2b5)
- [DT_GPIO_FLAGS](../hardware/P290_设备树GPIO宏.md#ga32b3383d7ed543602a7b4a031018316f)
- [DT_NUM_GPIO_HOGS](../hardware/P290_设备树GPIO宏.md#ga0a4575c3750db76692fd0f817a169b50)
- [DT_GPIO_HOG_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#gaf4ecdebbd433473f654f4b6859542af9)
- [DT_GPIO_HOG_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#gaed024e6acac49f591fe50cd43e8af14f)
- [DT_INST_GPIO_PIN_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga162bca126f7015816286358f09bde6ff)
- [DT_INST_GPIO_PIN](../hardware/P290_设备树GPIO宏.md#ga5ee13b3de1d4cecc877963dfa8820cfd)
- [DT_INST_GPIO_FLAGS_BY_IDX](../hardware/P290_设备树GPIO宏.md#gafd40d1eec5c1672b7675ae47388c1cef)
- [DT_INST_GPIO_FLAGS](../hardware/P290_设备树GPIO宏.md#ga8d3edd53d6d8e89afc68f0c10176f57f)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_GPIO设备树头文件源码.md)
