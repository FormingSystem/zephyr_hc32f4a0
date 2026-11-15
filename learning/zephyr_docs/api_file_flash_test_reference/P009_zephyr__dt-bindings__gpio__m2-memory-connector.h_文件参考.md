---
id: learning.zephyr-docs.api-file-flash-test-reference.page-9
title: zephyr__dt-bindings__gpio__m2-memory-connector.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_gpio\_\_m2-memory-connector.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

M.2 Key A串行存储器连接器（Serial Memory Connector）的引脚常量。

查看此文件的源码。

<a id="details"></a>

M.2 Key A串行存储器连接器（Serial Memory Connector）的引脚常量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_gaaf487da3f0d02501208b442e0279e5f7"></a>

```c
#define M2MEM_CONNECTOR_GPIO_SPI_SCK 16
```

相关声明：[M2MEM_CONNECTOR_GPIO_SPI_SCK](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaaf487da3f0d02501208b442e0279e5f7)。

可选辅助 SPI 时钟（Auxiliary SPI Clock）。

<a id="r_gaa521a518bdf14de7143eb0807946662b"></a>

```c
#define M2MEM_CONNECTOR_GPIO_SPI_MOSI 17
```

相关声明：[M2MEM_CONNECTOR_GPIO_SPI_MOSI](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaa521a518bdf14de7143eb0807946662b)。

可选辅助 SPI 控制器输出（Controller-out）。

<a id="r_ga465fddfb5ce88e1880e2b3c5ecd1c25b"></a>

```c
#define M2MEM_CONNECTOR_GPIO_LDO_EN 18
```

相关声明：[M2MEM_CONNECTOR_GPIO_LDO_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga465fddfb5ce88e1880e2b3c5ecd1c25b)。

必需的开漏 LDO 使能信号（Open-drain LDO Enable）。

<a id="r_gae423b100dfdc151191e6a38f5a420e69"></a>

```c
#define M2MEM_CONNECTOR_GPIO_SPI_MISO 19
```

相关声明：[M2MEM_CONNECTOR_GPIO_SPI_MISO](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gae423b100dfdc151191e6a38f5a420e69)。

可选辅助 SPI 控制器输入（Controller-in）。

<a id="r_gac46480baccb6fea25429ebd22ca11229"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCS2 20
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCS2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac46480baccb6fea25429ebd22ca11229)。

XSPI 片选（Chip Select） 2。

<a id="r_gaf95011fc4caf4ee6ee431cb0019a8a52"></a>

```c
#define M2MEM_CONNECTOR_GPIO_SPI_NSS 21
```

相关声明：[M2MEM_CONNECTOR_GPIO_SPI_NSS](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaf95011fc4caf4ee6ee431cb0019a8a52)。

可选辅助 SPI 片选（Chip Select）。

<a id="r_gac0baf71abac9556e79967cd056178cb9"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCS1 22
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCS1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac0baf71abac9556e79967cd056178cb9)。

XSPI 片选（Chip Select） 1。

<a id="r_ga01b4f31e760f2f14c5217fd37a03349f"></a>

```c
#define M2MEM_CONNECTOR_XSPI_DQS0 25
```

相关声明：[M2MEM_CONNECTOR_XSPI_DQS0](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga01b4f31e760f2f14c5217fd37a03349f)。

XSPI 数据选通（Data Strobe） 0。

<a id="r_ga8bc7b57ef1a523ef7fb30f0796ce6cb3"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D6 26
```

相关声明：[M2MEM_CONNECTOR_XSPI_D6](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga8bc7b57ef1a523ef7fb30f0796ce6cb3)。

XSPI 数据（Data） 6。

<a id="r_ga49787bb933caca32761c9047d2694a17"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D7 27
```

相关声明：[M2MEM_CONNECTOR_XSPI_D7](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga49787bb933caca32761c9047d2694a17)。

XSPI 数据（Data） 7。

<a id="r_gae41477f4ae5c801b86ddb19602a72086"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D5 28
```

相关声明：[M2MEM_CONNECTOR_XSPI_D5](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gae41477f4ae5c801b86ddb19602a72086)。

XSPI 数据（Data） 5。

<a id="r_ga056cb852a3fd93159c7034694ea5ae40"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D4 31
```

相关声明：[M2MEM_CONNECTOR_XSPI_D4](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga056cb852a3fd93159c7034694ea5ae40)。

XSPI 数据（Data） 4。

<a id="r_gabb974e553d90287a4f6cb1258fc21c69"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D3 32
```

相关声明：[M2MEM_CONNECTOR_XSPI_D3](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gabb974e553d90287a4f6cb1258fc21c69)。

XSPI 数据（Data） 3。

<a id="r_ga88664d2a94c4bee1b86bc21c87f76751"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D2 34
```

相关声明：[M2MEM_CONNECTOR_XSPI_D2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga88664d2a94c4bee1b86bc21c87f76751)。

XSPI 数据（Data） 2。

<a id="r_ga9ea4f4feb9fd1ae016102a3a5fe48704"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D1 35
```

相关声明：[M2MEM_CONNECTOR_XSPI_D1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga9ea4f4feb9fd1ae016102a3a5fe48704)。

XSPI 数据（Data） 1。

<a id="r_ga7800b4b86da2973fa9dd12607ee931e7"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D0 37
```

相关声明：[M2MEM_CONNECTOR_XSPI_D0](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7800b4b86da2973fa9dd12607ee931e7)。

XSPI 数据（Data） 0。

<a id="r_ga7c9a63541667f0d8f23599c4c2727c2c"></a>

```c
#define M2MEM_CONNECTOR_LED2 38
```

相关声明：[M2MEM_CONNECTOR_LED2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7c9a63541667f0d8f23599c4c2727c2c)。

红色 LED（LD2）。

<a id="r_ga9e0233afb0e3d2e6a03e4d6f4ac38820"></a>

```c
#define M2MEM_CONNECTOR_INT1 40
```

相关声明：[M2MEM_CONNECTOR_INT1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga9e0233afb0e3d2e6a03e4d6f4ac38820)。

可选的 GPIO、错误信号（Error）或中断（Interrupt）1。

<a id="r_ga17705fe5f4160f59e09a5e292148c9e0"></a>

```c
#define M2MEM_CONNECTOR_XSPI_CLK1 41
```

相关声明：[M2MEM_CONNECTOR_XSPI_CLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga17705fe5f4160f59e09a5e292148c9e0)。

XSPI 时钟（Clock） 1。

<a id="r_ga07f84d32126ce8e5f1d0caaf39ead910"></a>

```c
#define M2MEM_CONNECTOR_LED1 42
```

相关声明：[M2MEM_CONNECTOR_LED1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga07f84d32126ce8e5f1d0caaf39ead910)。

绿色 LED（LD1）。

<a id="r_ga0afd8831a609718f6593bc97da5d5dac"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCLK1 43
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga0afd8831a609718f6593bc97da5d5dac)。

XSPI 差分时钟互补信号（Differential Clock Complement） 1。

<a id="r_ga80f70d747e12d49bcc5a184044c36cd3"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D15 47
```

相关声明：[M2MEM_CONNECTOR_XSPI_D15](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga80f70d747e12d49bcc5a184044c36cd3)。

XSPI 数据（Data） 15。

<a id="r_ga0171d477a93fa59bc8e440827778eb6c"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D14 49
```

相关声明：[M2MEM_CONNECTOR_XSPI_D14](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga0171d477a93fa59bc8e440827778eb6c)。

XSPI 数据（Data） 14。

<a id="r_ga7f2678c5224456b8433ba603e67117eb"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCS4 52
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCS4](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7f2678c5224456b8433ba603e67117eb)。

XSPI 片选（Chip Select） 4。

<a id="r_ga14378f2107df4bd8f56e157b39688932"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D13 53
```

相关声明：[M2MEM_CONNECTOR_XSPI_D13](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga14378f2107df4bd8f56e157b39688932)。

XSPI 数据（Data） 13。

<a id="r_ga2d9e8d125f23078e7d2a0f257f34544d"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCS3 54
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCS3](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga2d9e8d125f23078e7d2a0f257f34544d)。

XSPI 片选（Chip Select） 3。

<a id="r_ga1c1b9acff7fac115f12324dc8d518315"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D12 55
```

相关声明：[M2MEM_CONNECTOR_XSPI_D12](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga1c1b9acff7fac115f12324dc8d518315)。

XSPI 数据（Data） 12。

<a id="r_gaf7dc26deef7119bf2ca45540fc7e27e5"></a>

```c
#define M2MEM_CONNECTOR_XSPI_DQS1 56
```

相关声明：[M2MEM_CONNECTOR_XSPI_DQS1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaf7dc26deef7119bf2ca45540fc7e27e5)。

XSPI 数据选通（Data Strobe） 1。

<a id="r_gac4f7feea9215881f5a6ccff3702e93ad"></a>

```c
#define M2MEM_CONNECTOR_I2C_SDA 58
```

相关声明：[M2MEM_CONNECTOR_I2C_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac4f7feea9215881f5a6ccff3702e93ad)。

用于标识 EEPROM 或辅助器件的 I2C 数据（I2C Data）。

<a id="r_gad20ec41251e5f1b8a4b8622f5ee94337"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D11 59
```

相关声明：[M2MEM_CONNECTOR_XSPI_D11](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gad20ec41251e5f1b8a4b8622f5ee94337)。

XSPI 数据（Data） 11。

<a id="r_gab056a94f06e8a8b89579b3343f37dbab"></a>

```c
#define M2MEM_CONNECTOR_I2C_SCL 60
```

相关声明：[M2MEM_CONNECTOR_I2C_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gab056a94f06e8a8b89579b3343f37dbab)。

用于标识 EEPROM 或辅助器件的 I2C 时钟（I2C Clock）。

<a id="r_ga90f8ddf4d5fdc82183fe099630b1f448"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D10 61
```

相关声明：[M2MEM_CONNECTOR_XSPI_D10](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga90f8ddf4d5fdc82183fe099630b1f448)。

XSPI 数据（Data） 10。

<a id="r_ga47afacd9314c5975004bcfd90dd6015c"></a>

```c
#define M2MEM_CONNECTOR_INT2 62
```

相关声明：[M2MEM_CONNECTOR_INT2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga47afacd9314c5975004bcfd90dd6015c)。

可选的 GPIO、错误信号（Error）或中断（Interrupt）2。

<a id="r_ga7275b54b1a6d2834cc277639e1f954e8"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D9 65
```

相关声明：[M2MEM_CONNECTOR_XSPI_D9](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7275b54b1a6d2834cc277639e1f954e8)。

XSPI 数据（Data） 9。

<a id="r_gad1b8522f7535761443e4035013f1b802"></a>

```c
#define M2MEM_CONNECTOR_NRST 66
```

相关声明：[M2MEM_CONNECTOR_NRST](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gad1b8522f7535761443e4035013f1b802)。

存储器复位（Memory Reset）。

<a id="r_ga7e421c1cbe9f130ad46b2a7273b80bf5"></a>

```c
#define M2MEM_CONNECTOR_XSPI_D8 67
```

相关声明：[M2MEM_CONNECTOR_XSPI_D8](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7e421c1cbe9f130ad46b2a7273b80bf5)。

XSPI 数据（Data） 8。

<a id="r_gafe6fd4096bd545b4a8ee8d9b27ee5ee2"></a>

```c
#define M2MEM_CONNECTOR_XSPI_CLK2 71
```

相关声明：[M2MEM_CONNECTOR_XSPI_CLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gafe6fd4096bd545b4a8ee8d9b27ee5ee2)。

XSPI 时钟（Clock） 2。

<a id="r_ga1c65aa7a07d9c25de8183cac589225cf"></a>

```c
#define M2MEM_CONNECTOR_XSPI_NCLK2 73
```

相关声明：[M2MEM_CONNECTOR_XSPI_NCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga1c65aa7a07d9c25de8183cac589225cf)。

XSPI 差分时钟互补信号（Differential Clock Complement） 2。


## 9.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P469_m2-memory-connector.h_源码浏览.md)
- [M2MEM_CONNECTOR_GPIO_SPI_SCK](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaaf487da3f0d02501208b442e0279e5f7)
- [M2MEM_CONNECTOR_GPIO_SPI_MOSI](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaa521a518bdf14de7143eb0807946662b)
- [M2MEM_CONNECTOR_GPIO_LDO_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga465fddfb5ce88e1880e2b3c5ecd1c25b)
- [M2MEM_CONNECTOR_GPIO_SPI_MISO](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gae423b100dfdc151191e6a38f5a420e69)
- [M2MEM_CONNECTOR_XSPI_NCS2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac46480baccb6fea25429ebd22ca11229)
- [M2MEM_CONNECTOR_GPIO_SPI_NSS](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaf95011fc4caf4ee6ee431cb0019a8a52)
- [M2MEM_CONNECTOR_XSPI_NCS1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac0baf71abac9556e79967cd056178cb9)
- [M2MEM_CONNECTOR_XSPI_DQS0](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga01b4f31e760f2f14c5217fd37a03349f)
- [M2MEM_CONNECTOR_XSPI_D6](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga8bc7b57ef1a523ef7fb30f0796ce6cb3)
- [M2MEM_CONNECTOR_XSPI_D7](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga49787bb933caca32761c9047d2694a17)
- [M2MEM_CONNECTOR_XSPI_D5](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gae41477f4ae5c801b86ddb19602a72086)
- [M2MEM_CONNECTOR_XSPI_D4](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga056cb852a3fd93159c7034694ea5ae40)
- [M2MEM_CONNECTOR_XSPI_D3](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gabb974e553d90287a4f6cb1258fc21c69)
- [M2MEM_CONNECTOR_XSPI_D2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga88664d2a94c4bee1b86bc21c87f76751)
- [M2MEM_CONNECTOR_XSPI_D1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga9ea4f4feb9fd1ae016102a3a5fe48704)
- [M2MEM_CONNECTOR_XSPI_D0](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7800b4b86da2973fa9dd12607ee931e7)
- [M2MEM_CONNECTOR_LED2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7c9a63541667f0d8f23599c4c2727c2c)
- [M2MEM_CONNECTOR_INT1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga9e0233afb0e3d2e6a03e4d6f4ac38820)
- [M2MEM_CONNECTOR_XSPI_CLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga17705fe5f4160f59e09a5e292148c9e0)
- [M2MEM_CONNECTOR_LED1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga07f84d32126ce8e5f1d0caaf39ead910)
- [M2MEM_CONNECTOR_XSPI_NCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga0afd8831a609718f6593bc97da5d5dac)
- [M2MEM_CONNECTOR_XSPI_D15](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga80f70d747e12d49bcc5a184044c36cd3)
- [M2MEM_CONNECTOR_XSPI_D14](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga0171d477a93fa59bc8e440827778eb6c)
- [M2MEM_CONNECTOR_XSPI_NCS4](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7f2678c5224456b8433ba603e67117eb)
- [M2MEM_CONNECTOR_XSPI_D13](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga14378f2107df4bd8f56e157b39688932)
- [M2MEM_CONNECTOR_XSPI_NCS3](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga2d9e8d125f23078e7d2a0f257f34544d)
- [M2MEM_CONNECTOR_XSPI_D12](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga1c1b9acff7fac115f12324dc8d518315)
- [M2MEM_CONNECTOR_XSPI_DQS1](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gaf7dc26deef7119bf2ca45540fc7e27e5)
- [M2MEM_CONNECTOR_I2C_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gac4f7feea9215881f5a6ccff3702e93ad)
- [M2MEM_CONNECTOR_XSPI_D11](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gad20ec41251e5f1b8a4b8622f5ee94337)
- [M2MEM_CONNECTOR_I2C_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gab056a94f06e8a8b89579b3343f37dbab)
- [M2MEM_CONNECTOR_XSPI_D10](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga90f8ddf4d5fdc82183fe099630b1f448)
- [M2MEM_CONNECTOR_INT2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga47afacd9314c5975004bcfd90dd6015c)
- [M2MEM_CONNECTOR_XSPI_D9](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7275b54b1a6d2834cc277639e1f954e8)
- [M2MEM_CONNECTOR_NRST](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gad1b8522f7535761443e4035013f1b802)
- [M2MEM_CONNECTOR_XSPI_D8](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga7e421c1cbe9f130ad46b2a7273b80bf5)
- [M2MEM_CONNECTOR_XSPI_CLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#gafe6fd4096bd545b4a8ee8d9b27ee5ee2)
- [M2MEM_CONNECTOR_XSPI_NCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html#ga1c65aa7a07d9c25de8183cac589225cf)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__sensor__ltc4286.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__bluetooth__mesh__main.h_文件参考.md)
