---
id: learning.zephyr-docs.api-file-host-video-reference.page-3
title: zephyr__drivers__mipi_dbi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_mipi\_dbi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MIPI显示总线接口（Display Bus Interface，MIPI-DBI）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/display.h>
#include <zephyr/display/mipi_display.h>
#include <zephyr/drivers/spi.h>
#include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>
```

查看此文件的源码。

MIPI 显示总线接口（MIPI-DBI，Display Bus Interface）驱动 API 的主头文件。MIPI-DBI 定义三种接口：Type A 为 Motorola 6800 型并行总线；Type B 为 Intel 8080 型并行总线；Type C 为 SPI 型单比特总线，提供三种选项：每字节使用 9 个写时钟，最后一位是命令／数据选择位；与前者类似，但每字节使用 16 个写时钟；每字节使用 8 个写时钟，并通过 GPIO 引脚选择命令／数据。当前驱动接口不支持每字节 16 个写时钟的 Type C 选项 2。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_mipi_5Fdbi_5Fconfig"></a>

```c
struct mipi_dbi_config
```

相关声明：[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)。

MIPI显示总线接口（DBI）的控制器配置。

<a id="r_mipi_5Fdbi_5Fdriver_5Fapi"></a>

```c
struct mipi_dbi_driver_api
```

相关声明：[mipi_dbi_driver_api](../hardware/P252_MIPI显示总线函数表.md)。

驱动操作（Driver Operations）：MIPI显示总线接口（MIPI-DBI）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga883d37df02699ddd102c020499f25698"></a>

```c
#define MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id)
```

相关声明：[MIPI_DBI_SPI_DEV_HAS_CS_GPIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga883d37df02699ddd102c020499f25698)。

检查 MIPI DBI SPI 设备是否配置了片选线（Chip Select Line）。

<a id="r_ga9e05938ce1cd2b647cb00a77b773ad1d"></a>

```c
#define MIPI_DBI_SPI_CONFIG_DT(node_id, operation_, delay_)
```

相关声明：[MIPI_DBI_SPI_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga9e05938ce1cd2b647cb00a77b773ad1d)。

根据设备树（Devicetree）初始化 MIPI DBI SPI 配置结构体。

<a id="r_ga93d0c043dc9022bbe42c21a13bc46091"></a>

```c
#define MIPI_DBI_SPI_CONFIG_DT_INST(inst, operation_, delay_)
```

相关声明：[MIPI_DBI_SPI_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga93d0c043dc9022bbe42c21a13bc46091)。

根据设备树实例（Devicetree Instance）初始化 MIPI DBI SPI 配置。

<a id="r_ga94aed5adf0dc393556b2c8c9976aeddf"></a>

```c
#define MIPI_DBI_CONFIG_DT(node_id, operation_, delay_)
```

相关声明：[MIPI_DBI_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga94aed5adf0dc393556b2c8c9976aeddf)。

根据设备树（Devicetree）初始化 MIPI DBI 配置。

<a id="r_ga658456683f895d3b44ea44d9bf8b0558"></a>

```c
#define MIPI_DBI_CONFIG_DT_INST(inst, operation_, delay_)
```

相关声明：[MIPI_DBI_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga658456683f895d3b44ea44d9bf8b0558)。

根据设备实例（Device Instance）初始化 MIPI DBI 配置。

<a id="r_ga0e60d22a8172d1a0b017707eccdc6c7e"></a>

```c
#define MIPI_DBI_TE_MODE_DT(node_id, edge_prop)
```

相关声明：[MIPI_DBI_TE_MODE_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga0e60d22a8172d1a0b017707eccdc6c7e)。

从设备树（Devicetree）获取 MIPI DBI 的撕裂效应信号模式（TE Mode）。

<a id="r_gaec5f771a41fa75072b9e79ce125876a7"></a>

```c
#define MIPI_DBI_TE_MODE_DT_INST(inst, edge_prop)
```

相关声明：[MIPI_DBI_TE_MODE_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaec5f771a41fa75072b9e79ce125876a7)。

获取设备实例的 MIPI DBI 撕裂效应信号模式（TE Mode）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga3ea6251e2fe3a18c8daba66c4ded41d6"></a>

```c
typedef int(* mipi_dbi_command_write_t) (const struct device *dev, const struct mipi_dbi_config *config, uint8_t cmd, const uint8_t *data, size_t len)
```

相关声明：[mipi_dbi_command_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga3ea6251e2fe3a18c8daba66c4ded41d6)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向显示控制器写入命令的回调 API（Callback API）。

<a id="r_ga7c6f09c6fece9c343aa4717150ca170e"></a>

```c
typedef int(* mipi_dbi_command_read_t) (const struct device *dev, const struct mipi_dbi_config *config, uint8_t *cmds, size_t num_cmds, uint8_t *response, size_t len)
```

相关声明：[mipi_dbi_command_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga7c6f09c6fece9c343aa4717150ca170e)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从显示控制器读取命令响应的回调 API（Callback API）。

<a id="r_gad973c1d30050ea3b6c3f9e1032e5383c"></a>

```c
typedef int(* mipi_dbi_write_display_t) (const struct device *dev, const struct mipi_dbi_config *config, const uint8_t *framebuf, struct display_buffer_descriptor *desc, enum display_pixel_format pixfmt)
```

相关声明：[mipi_dbi_write_display_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#gad973c1d30050ea3b6c3f9e1032e5383c)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

向显示控制器写入显示缓冲区的回调 API（Callback API）。

<a id="r_ga37ac264a3130d34a8d594c7482b09870"></a>

```c
typedef int(* mipi_dbi_reset_t) (const struct device *dev, k_timeout_t delay)
```

相关声明：[mipi_dbi_reset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga37ac264a3130d34a8d594c7482b09870)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

复位所连接显示控制器的回调 API（Callback API）。

<a id="r_ga12f0446626ab4feb996f33fcea4129dd"></a>

```c
typedef int(* mipi_dbi_release_t) (const struct device *dev, const struct mipi_dbi_config *config)
```

相关声明：[mipi_dbi_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga12f0446626ab4feb996f33fcea4129dd)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)。

释放已锁定 MIPI DBI 设备的回调 API（Callback API）。

<a id="r_ga2000c1dc2ac1efe0eb6179a18da1e5c2"></a>

```c
typedef int(* mipi_dbi_configure_te_t) (const struct device *dev, uint8_t edge, k_timeout_t delay)
```

相关声明：[mipi_dbi_configure_te_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga2000c1dc2ac1efe0eb6179a18da1e5c2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

配置 MIPI DBI 撕裂效应信号（Tearing Effect Signal）的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gad36e3d57fd931236c4ed4e58dfef1cca"></a>

```c
static int mipi_dbi_command_write (const struct device *dev, const struct mipi_dbi_config *config, uint8_t cmd, const uint8_t *data, size_t len)
```

相关声明：[mipi_dbi_command_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向显示控制器（Display Controller）写入命令。

<a id="r_gafac64feca9fdee3803154bacb58e8e47"></a>

```c
static int mipi_dbi_command_read (const struct device *dev, const struct mipi_dbi_config *config, uint8_t *cmds, size_t num_cmd, uint8_t *response, size_t len)
```

相关声明：[mipi_dbi_command_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafac64feca9fdee3803154bacb58e8e47)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从显示控制器（Display Controller）读取命令响应。

<a id="r_ga62aa7b9677da010a678580d956f7d0e3"></a>

```c
static int mipi_dbi_write_display (const struct device *dev, const struct mipi_dbi_config *config, const uint8_t *framebuf, struct display_buffer_descriptor *desc, enum display_pixel_format pixfmt)
```

相关声明：[mipi_dbi_write_display](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

向显示控制器（Display Controller）写入显示缓冲区。

<a id="r_ga1c1a117ae5db5f7508f302d48dc72013"></a>

```c
static int mipi_dbi_reset (const struct device *dev, uint32_t delay_ms)
```

相关声明：[mipi_dbi_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga1c1a117ae5db5f7508f302d48dc72013)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

复位所连接的显示控制器（Display Controller）。

<a id="r_gade0b635bcd4f16fb3ec5d122d1b09161"></a>

```c
static int mipi_dbi_release (const struct device *dev, const struct mipi_dbi_config *config)
```

相关声明：[mipi_dbi_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161)、[device](../device_reference/P002_设备对象结构.md)、[mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)。

释放已锁定的 MIPI DBI 设备（Locked Device）。

<a id="r_gab74f96d99f9702f29b51cc2fe0b48d95"></a>

```c
static int mipi_dbi_configure_te (const struct device *dev, uint8_t edge, uint32_t delay_us)
```

相关声明：[mipi_dbi_configure_te](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab74f96d99f9702f29b51cc2fe0b48d95)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 MIPI DBI 撕裂效应信号（Tearing Effect Signal）。


## 3.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [zephyr/display/mipi_display.h](../api_source_reference/P531_mipi_display.h_源码浏览.md)
- [zephyr/drivers/spi.h](../spi_driver_reference/P002_SPI驱动头文件源码.md)
- [zephyr/dt-bindings/mipi_dbi/mipi_dbi.h](../api_source_reference/P191_mipi_dbi.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P164_mipi_dbi.h_源码浏览.md)
- [mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)
- [mipi_dbi_driver_api](../hardware/P252_MIPI显示总线函数表.md)
- [MIPI_DBI_SPI_DEV_HAS_CS_GPIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga883d37df02699ddd102c020499f25698)
- [MIPI_DBI_SPI_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga9e05938ce1cd2b647cb00a77b773ad1d)
- [MIPI_DBI_SPI_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga93d0c043dc9022bbe42c21a13bc46091)
- [MIPI_DBI_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga94aed5adf0dc393556b2c8c9976aeddf)
- [MIPI_DBI_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga658456683f895d3b44ea44d9bf8b0558)
- [MIPI_DBI_TE_MODE_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga0e60d22a8172d1a0b017707eccdc6c7e)
- [MIPI_DBI_TE_MODE_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaec5f771a41fa75072b9e79ce125876a7)
- [mipi_dbi_command_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga3ea6251e2fe3a18c8daba66c4ded41d6)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mipi_dbi_command_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga7c6f09c6fece9c343aa4717150ca170e)
- [mipi_dbi_write_display_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#gad973c1d30050ea3b6c3f9e1032e5383c)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [mipi_dbi_reset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga37ac264a3130d34a8d594c7482b09870)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mipi_dbi_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga12f0446626ab4feb996f33fcea4129dd)
- [mipi_dbi_configure_te_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga2000c1dc2ac1efe0eb6179a18da1e5c2)
- [mipi_dbi_command_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca)
- [mipi_dbi_command_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafac64feca9fdee3803154bacb58e8e47)
- [mipi_dbi_write_display](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3)
- [mipi_dbi_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga1c1a117ae5db5f7508f302d48dc72013)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mipi_dbi_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161)
- [mipi_dbi_configure_te](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab74f96d99f9702f29b51cc2fe0b48d95)

<a id="header-details"></a>

---

[上一章](P002_zephyr__net__coap_service.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__pcie__pcie.h_文件参考.md)
