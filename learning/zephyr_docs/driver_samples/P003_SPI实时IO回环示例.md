---
id: learning.zephyr-docs.driver_samples.page-3
title: SPI实时IO回环示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/spi/rtio_loopback/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="spi-rtio-loopback"></a>

# 第3章\_SPI实时IO回环示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/spi/rtio_loopback/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 3.1\_概览（Overview）

本例演示通过实时输入输出（Real-Time I/O，RTIO）执行串行外设接口（Serial Peripheral Interface，SPI）传输。使用两个SPI控制器硬件，分别工作为总线控制端（Controller）与外设／目标端（Peripheral／Target）。

<a id="requirements"></a>

## 3.2\_要求（Requirements）

需要两个SPI控制器：一个支持控制端角色，另一个支持外设／目标端角色，并连接到同一条SPI总线。

**注意：**务必实际连接相关SPI控制器与总线；设备树声明不能代替物理接线。

<a id="board-support"></a>

## 3.3\_开发板支持（Board support）

满足条件的板应提供设备树覆盖文件（Overlay），指定两端角色：在相应控制器下添加SPI设备子节点，为控制端视角的设备节点设置 `spi_controller` 标签，为目标端视角的设备节点设置 `spi_target` 标签。两节点分别从控制端和目标端视角描述同一个SPI设备。

```dts
&spi22 {
        status = "okay";
        cs-gpios = <&gpio2 10 GPIO_ACTIVE_LOW>;

        spi_controller: spi-device@0 {
                   compatible = "vnd,spi-device";
                   reg = <0>;
                   spi-max-frequency = <DT_FREQ_M(8)>;
        };
};

&spi21 {
        status = "okay";

        spi_target: spi-device@0 {
                   compatible = "vnd,spi-device";
                   reg = <0>;
                   spi-max-frequency = <DT_FREQ_M(8)>;
        };
};
```

必要时，在板专用配置片段（Configuration Fragment）中加入相应选项，例如：

```kconfig
CONFIG_SPI_STM32_INTERRUPT=y
```

> 译注——节点和配置边界：标签位于spi-device子节点，不是把控制器本身改名。spi22、spi21、gpio2及片选引脚10均属于原配置示例，应按实际硬件接线选择；CONFIG_SPI_STM32_INTERRUPT是STM32专用示例选项，不适用于所有驱动。

<a id="transferred-data-sizes"></a>

## 3.4\_传输数据大小（Transferred data sizes）

原页列出以下示例专用配置，可调整测试传输：

| 配置项 | 含义 |
| --- | --- |
| `CONFIG_SAMPLE_DATA_WRITE_SIZE` | 控制端视角的写入字节数 |
| `CONFIG_SAMPLE_DATA_READ_SIZE` | 控制端视角的读取字节数 |
| `CONFIG_SAMPLE_SPI_MODE_0` | SPI模式0 |
| `CONFIG_SAMPLE_SPI_MODE_1` | SPI模式1 |
| `CONFIG_SAMPLE_SPI_MODE_2` | SPI模式2 |
| `CONFIG_SAMPLE_SPI_MODE_3` | SPI模式3 |
| `CONFIG_SAMPLE_SPI_BIT_ORDER_MSB` | 最高有效位优先（Most Significant Bit First） |
| `CONFIG_SAMPLE_SPI_BIT_ORDER_LSB` | 最低有效位优先（Least Significant Bit First） |

> 译注——配置分类：所读[示例Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi/rtio_loopback/Kconfig)把前两项定义为字节数量，默认分别为4和32；模式0—3属于一组choice，MSB／LSB属于另一组choice，后六项并非大小参数。原页没有提供构建命令或成功日志，本译文不虚构已运行结果。

<a id="see-also"></a>

## 3.5\_相关接口（See also）

[RTIO接口](../rtio_core_reference/P001_RTIO公共接口.md)、[SPI接口](../hardware/P318_SPI公共接口.md)。


对应官方文档源码：[samples/drivers/spi/rtio_loopback/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi/rtio_loopback/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/spi/rtio_loopback/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/spi/rtio_loopback/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P002_GPIO按钮中断示例.md) · [返回大纲](大纲.md) · [下一章](P004_SPI软件模拟示例.md)
