---
id: learning.zephyr-docs.dt-peripheral-reference.page-4
title: SPI设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2spi_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_SPI设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2spi_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_SPI设备树头文件参考.md)和[公共API](../hardware/P329_SPI设备树宏.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00079"></a>
<a id="foldopen00118"></a>
<a id="foldopen00152"></a>
<a id="foldopen00185"></a>
<a id="foldopen00213"></a>
<a id="foldopen00223"></a>
<a id="foldopen00233"></a>
<a id="foldopen00242"></a>
<a id="foldopen00252"></a>

<pre><code class="language-c"><a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>/*
<a id="l00007"></a> * Copyright (c) 2020 Nordic Semiconductor
<a id="l00008"></a> *
<a id="l00009"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00010"></a> */
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_SPI_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_DEVICETREE_SPI_H_
<a id="l00014"></a>
<a id="l00015"></a>#ifdef __cplusplus
<a id="l00016"></a>extern "C" {
<a id="l00017"></a>#endif
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00053"></a>#define DT_SPI_HAS_CS_GPIOS(spi) DT_NODE_HAS_PROP(spi, cs_gpios)
<a id="l00054"></a>
<a id="l00079"></a>#define DT_SPI_NUM_CS_GPIOS(spi) \
<a id="l00080"></a>        COND_CODE_1(DT_SPI_HAS_CS_GPIOS(spi), \
<a id="l00081"></a>                    (DT_PROP_LEN(spi, cs_gpios)), (0))
<a id="l00082"></a>
<a id="l00118"></a>#define DT_SPI_DEV_HAS_CS_GPIOS(spi_dev)                                                           \
<a id="l00119"></a>        DT_PROP_HAS_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
<a id="l00120"></a>
<a id="l00152"></a>#define DT_SPI_DEV_CS_GPIOS_CTLR(spi_dev) \
<a id="l00153"></a>        DT_GPIO_CTLR_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
<a id="l00154"></a>
<a id="l00185"></a>#define DT_SPI_DEV_CS_GPIOS_PIN(spi_dev) \
<a id="l00186"></a>        DT_GPIO_PIN_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
<a id="l00187"></a>
<a id="l00213"></a>#define DT_SPI_DEV_CS_GPIOS_FLAGS(spi_dev) \
<a id="l00214"></a>        DT_GPIO_FLAGS_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
<a id="l00215"></a>
<a id="l00223"></a>#define DT_INST_SPI_DEV_HAS_CS_GPIOS(inst) \
<a id="l00224"></a>        DT_SPI_DEV_HAS_CS_GPIOS(DT_DRV_INST(inst))
<a id="l00225"></a>
<a id="l00233"></a>#define DT_INST_SPI_DEV_CS_GPIOS_CTLR(inst) \
<a id="l00234"></a>        DT_SPI_DEV_CS_GPIOS_CTLR(DT_DRV_INST(inst))
<a id="l00235"></a>
<a id="l00242"></a>#define DT_INST_SPI_DEV_CS_GPIOS_PIN(inst) \
<a id="l00243"></a>        DT_SPI_DEV_CS_GPIOS_PIN(DT_DRV_INST(inst))
<a id="l00244"></a>
<a id="l00252"></a>#define DT_INST_SPI_DEV_CS_GPIOS_FLAGS(inst) \
<a id="l00253"></a>        DT_SPI_DEV_CS_GPIOS_FLAGS(DT_DRV_INST(inst))
<a id="l00254"></a>
<a id="l00258"></a>
<a id="l00259"></a>#ifdef __cplusplus
<a id="l00260"></a>}
<a id="l00261"></a>#endif
<a id="l00262"></a>
<a id="l00263"></a>#endif  /* ZEPHYR_INCLUDE_DEVICETREE_SPI_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2020 Nordic Semiconductor；Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_SPI_H_。

## 4.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 4.4\_源码跟踪译注

> 译注——片选索引来自reg：设备版本先通过DT_BUS(spi_dev)找到SPI总线节点，再以设备第0个reg的原始值DT_REG_ADDR_RAW(spi_dev)作为总线cs-gpios的条目索引。这里的reg是SPI从设备片选编号，不是CPU寄存器基地址，也不是该设备在子节点列表中的顺序。控制器、引脚和flags读取同一条目。

> 译注——有GPIO片选与可用SPI不同：DT_SPI_HAS_CS_GPIOS只检查控制器属性存在，NUM版本缺失时为0；DEV_HAS版本检查该设备索引对应的cs-gpios条目。没有GPIO片选不代表控制器不支持硬件片选，也不能据此判断SPI传输是否可用。读取片选宏不拉高或拉低引脚，不执行传输。

> 译注——先区分对象：DT_SPI_HAS_CS_GPIOS与NUM接收控制器节点，DT_SPI_DEV_*接收SPI设备节点，DT_INST_SPI_DEV_*再以DT_DRV_COMPAT转换实例。名字相近但对象层次不同，不应把总线控制器作为从设备传给DEV版本。

> 译注——版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

头文件相对定位：[include/zephyr/devicetree/spi.h](../../../include/zephyr/devicetree/spi.h)，关联实现／接口：[include/zephyr/devicetree/gpio.h](../../../include/zephyr/devicetree/gpio.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/spi.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/gpio.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_SPI设备树头文件参考.md)

---

[上一章](P003_SPI设备树头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_CAN设备树头文件参考.md)
