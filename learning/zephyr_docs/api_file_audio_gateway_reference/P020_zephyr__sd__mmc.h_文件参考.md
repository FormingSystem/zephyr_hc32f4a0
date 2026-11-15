---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-20
title: zephyr__sd__mmc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_sd\_\_mmc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多媒体卡（MMC）存储卡子系统的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/sd/sd.h>
```

查看此文件的源码。

多媒体卡（MMC）存储卡子系统的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_acc996d4fba8673401816a7b41707b96f"></a>

```c
int mmc_write_blocks (struct sd_card *card, const uint8_t *wbuf, uint32_t start_block, uint32_t num_blocks)
```

相关声明：[mmc_write_blocks](#acc996d4fba8673401816a7b41707b96f)、[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将缓冲区中的块写入 MMC 卡（MMC Card）。

<a id="r_aa890ebd312875906583d56ddb1a03560"></a>

```c
int mmc_read_blocks (struct sd_card *card, uint8_t *rbuf, uint32_t start_block, uint32_t num_blocks)
```

相关声明：[mmc_read_blocks](#aa890ebd312875906583d56ddb1a03560)、[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 MMC 卡读取块到缓冲区。

<a id="r_a2dd835a0e88299400cd1b4e1533a7b4b"></a>

```c
int mmc_ioctl (struct sd_card *card, uint8_t cmd, void *buf)
```

相关声明：[mmc_ioctl](#a2dd835a0e88299400cd1b4e1533a7b4b)、[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

从 MMC 卡获取 I/O 控制数据（I/O Control Data）。

## 20.2\_详细说明（Detailed Documentation）

<a id="a2dd835a0e88299400cd1b4e1533a7b4b"></a>

### `mmc_ioctl()`

```c
int mmc_ioctl ( struct sd_card * card, uint8_t cmd, void * buf )
```

从 MMC 卡获取 I/O 控制数据（I/O Control Data）。

向 MMC 卡发送 I/O 控制命令（I/O Control Commands）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `card` | MMC 卡（MMC Card） |
| `cmd` | I/O 控制命令（I/O Control Command），与磁盘子系统一致；可用命令列表参见 include/zephyr/drivers/disk.h。 |
| `buf` | I/O 控制缓冲区（I/O Control Buffer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | I/O 控制命令（IOCTL Command）成功。 |
| `-ENOTSUP` | 不支持的 I/O 控制命令（IOCTL Command）。 |
| `-EIO` | I/O 失败（I/O Failure）。 |

<a id="aa890ebd312875906583d56ddb1a03560"></a>

### `mmc_read_blocks()`

```c
int mmc_read_blocks ( struct sd_card * card, uint8_t * rbuf, uint32_t start_block, uint32_t num_blocks )
```

从 MMC 卡读取块到缓冲区。

从 MMC 卡读取多个块到 MMC 缓冲区。为取得最佳性能，此缓冲区应按 CONFIG_SDHC_BUFFER_ALIGNMENT 对齐。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `card` | 要读取的 MMC 卡 |
| `rbuf` | 读取缓冲区（Read Buffer） |
| `start_block` | 读取的起始块（First Block） |
| `num_blocks` | 要读取的块数 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡读取超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="acc996d4fba8673401816a7b41707b96f"></a>

### `mmc_write_blocks()`

```c
int mmc_write_blocks ( struct sd_card * card, const uint8_t * wbuf, uint32_t start_block, uint32_t num_blocks )
```

将缓冲区中的块写入 MMC 卡（MMC Card）。

将 MMC 缓冲区中的多个块写入 MMC 卡。为取得最佳性能，此缓冲区应按 CONFIG_SDHC_BUFFER_ALIGNMENT 对齐。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `card` | 要写入的 MMC 卡 |
| `wbuf` | 写缓冲区（Write Buffer）。 |
| `start_block` | 写入的起始块（First Block） |
| `num_blocks` | 要写入的块数 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |


## 20.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sdhc.h](../peripheral_bus_storage_source_reference/P025_zephyr__drivers__sdhc.h_头文件源码.md)
- [zephyr/sd/sd.h](../peripheral_bus_storage_source_reference/P024_zephyr__sd__sd.h_头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P537_mmc.h_源码浏览.md)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [include/zephyr/drivers/disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_zephyr__drivers__interrupt_controller__intc_infineon_aurix.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__net__mqtt_sn.h_文件参考.md)
