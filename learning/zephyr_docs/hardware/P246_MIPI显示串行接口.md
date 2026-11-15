---
id: learning.zephyr-docs.hardware.mipi-2
title: MIPI显示串行接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第246章\_MIPI显示串行接口

原文：[group__mipi__dsi__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html)。读取日期：2026-10-13，`latest`。

## 246.1\_范围与版本

本页定义 MIPI **显示串行接口（Display Serial Interface，DSI）**的驱动 **应用程序编程接口（Application Programming Interface，API）**，自 Zephyr 3.1 提供，本页版本为 1.0.0。主头文件为 `zephyr/drivers/mipi_dsi.h`；像素格式常量来自 `zephyr/dt-bindings/mipi_dsi/mipi_dsi.h`。

配套结构为[显示时序](P248_MIPI显示串行时序.md)、[设备描述](P249_MIPI显示串行设备.md)和[读写消息](P250_MIPI显示串行消息.md)。驱动实现者另见[DSI后端接口](P253_MIPI显示串行后端.md)。

## 246.2\_设备模式标志

以下均为宏定义。`BIT(n)` 表示第 n 位掩码。VSync/HSync 分别为垂直/水平同步（Vertical/Horizontal Synchronization）；前肩/后肩（Front Porch/Back Porch）指同步时序相应区段；FIFO 为先进先出缓冲区（First In, First Out）；HS 是高速模式（High-Speed Mode）；EoT 为传输结束（End of Transmission）；LPM 为低功耗模式（Low-Power Mode）。

| 宏 | 值 | 原文含义 |
| --- | --- | --- |
| [`MIPI_DSI_MODE_VIDEO`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga2b4ff0fda3d00061b06e576a98628e7b) | `BIT(0)` | 视频模式（Video Mode）。 |
| [`MIPI_DSI_MODE_VIDEO_BURST`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaabfe30e5981efc1a73f4f9bf2def1610) | `BIT(1)` | 视频突发模式（Video Burst Mode）。 |
| [`MIPI_DSI_MODE_VIDEO_SYNC_PULSE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75709f3a91b803598d9d772f3c5b9eed) | `BIT(2)` | 视频脉冲模式（Video Pulse Mode）。 |
| [`MIPI_DSI_MODE_VIDEO_AUTO_VERT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5871aadda35ece0944217053f5c6c6fe) | `BIT(3)` | 启用自动垂直计数模式。 |
| [`MIPI_DSI_MODE_VIDEO_HSE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga21d9620a4986884bbe2ac3a11b311337) | `BIT(4)` | 在垂直同步脉冲及垂直肩区启用水平同步结束包（HSync-End Packets）。 |
| [`MIPI_DSI_MODE_VIDEO_HFP`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga625d1738ae1cfd25aef5772729c0aae8) | `BIT(5)` | **禁用**水平前肩区（Horizontal Front Porch）。 |
| [`MIPI_DSI_MODE_VIDEO_HBP`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga90e09b889a1dbac1e2b7b9ae84f38ee4) | `BIT(6)` | **禁用**水平后肩区（Horizontal Back Porch）。 |
| [`MIPI_DSI_MODE_VIDEO_HSA`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga395bb9085f92a1927e3cc317196ab353) | `BIT(7)` | **禁用**水平同步有效区（HSync Active Area）。 |
| [`MIPI_DSI_MODE_VSYNC_FLUSH`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gacdc35d8e6726accc88c2e2e82c88d46d) | `BIT(8)` | 在垂直同步脉冲时刷新显示 FIFO。 |
| [`MIPI_DSI_MODE_EOT_PACKET`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga4bbcabcb84af1a2bd715b0bd8be78db3) | `BIT(9)` | 在 HS 模式下**禁用** EoT 包。 |
| [`MIPI_DSI_CLOCK_NON_CONTINUOUS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75c0e183f1235e37245cf890aa4a656b) | `BIT(10)` | 设备支持非连续时钟行为，原文引用 DSI 规范第5.6.1节。 |
| [`MIPI_DSI_MODE_LPM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga1f8923811fc5d704e28362e72a1f1633) | `BIT(11)` | 以低功耗方式传输数据。 |

## 246.3\_消息标志与像素格式

宏 [`MIPI_DSI_MSG_USE_LPM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaaf7954dcd5644e3ff332f5fab8fe48ef) 定义为 `BIT(0x0)`。原文只列出定义，没有附加文字描述。

RGB 表示红、绿、蓝（Red, Green, Blue）；bpp 是每像素位数（Bits per Pixel）。RGB888、RGB666、RGB565 的三个数字依次表示红、绿、蓝的有效分量位数，实际传输位数由是否打包决定。像素格式宏如下：

| 宏 | 值 | 格式 |
| --- | --- | --- |
| [`MIPI_DSI_PIXFMT_RGB888`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gafb9cb05fbca552449bab635544517d25) | `0U` | RGB888，24 bpp。 |
| [`MIPI_DSI_PIXFMT_RGB666`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad7288299bb5248e8fab55d07c310cd85) | `1U` | RGB666，24 bpp。 |
| [`MIPI_DSI_PIXFMT_RGB666_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gadad1c9a93585a16c643bc33ef280b38b) | `2U` | 打包 RGB666（Packed RGB666），18 bpp。 |
| [`MIPI_DSI_PIXFMT_RGB565`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gab74cc16bec1613c5e1eff30de2aa25c6) | `3U` | RGB565，16 bpp。 |

> 译注：普通 RGB666 与打包 RGB666 的传输位数不同，保留原文 24 bpp 与 18 bpp 的区别。

## 246.4\_连接与分离设备

函数 [`mipi_dsi_attach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga18689fac223fddc10b23b6bc6712944e) 将新设备连接到总线，函数 [`mipi_dsi_detach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace728ac82d30e15868298facd6df0228) 将设备从总线分离：

```c
static inline int mipi_dsi_attach(const struct device *dev, uint8_t channel,
                                  const struct mipi_dsi_device *mdev);
static inline int mipi_dsi_detach(const struct device *dev, uint8_t channel,
                                  const struct mipi_dsi_device *mdev);
```

`dev` 为 MIPI DSI 主机设备（Host Device），`channel` 为设备通道（Device Channel，原文记为 VID），`mdev` 为 DSI 设备描述。两者成功返回 0，出错返回负值。

## 246.5\_消息传输

函数 [`mipi_dsi_transfer()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace5bb52f483634baa185f46ac61efb71) 向连接在总线上的设备传输数据，或从该设备接收数据：

```c
static inline ssize_t mipi_dsi_transfer(const struct device *dev,
                                        uint8_t channel, struct mipi_dsi_msg *msg);
```

`dev` 是 MIPI DSI 设备，`channel` 是设备通道，`msg` 是消息。成功返回传输的数据大小，出错返回负值；返回类型 [`ssize_t`](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118) 可表示大小或负错误值。

## 246.6\_通用读写

```c
ssize_t mipi_dsi_generic_read(const struct device *dev, uint8_t channel,
    const void *params, size_t nparams, void *buf, size_t len);
ssize_t mipi_dsi_generic_write(const struct device *dev, uint8_t channel,
                              const void *buf, size_t len);
```

函数 [`mipi_dsi_generic_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga121633e8e379e7d1ebd749328f2014fd) 执行通用读取（Generic Read）：`dev` 为主机设备，`channel` 为设备通道，`params` 指向请求参数缓冲区，`nparams` 为参数数量，`buf` 为存放读出数据的缓冲区，`len` 为接收缓冲区长度。成功返回读取的数据大小，出错返回负值。

函数 [`mipi_dsi_generic_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5442f45c7c827d1dd8c3fa21da49c560) 执行通用写入（Generic Write）：`dev` 和 `channel` 含义同上，`buf` 是发送缓冲区，`len` 是发送缓冲区长度。成功返回写入的数据大小，出错返回负值。

## 246.7\_显示命令集读写

DCS 表示显示命令集（Display Command Set），命令常量见[MIPI显示接口定义](P244_MIPI显示接口定义.md)。

```c
ssize_t mipi_dsi_dcs_read(const struct device *dev, uint8_t channel,
                         uint8_t cmd, void *buf, size_t len);
ssize_t mipi_dsi_dcs_write(const struct device *dev, uint8_t channel,
                          uint8_t cmd, const void *buf, size_t len);
```

函数 [`mipi_dsi_dcs_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga7b5f52bcd51821bf120c5ac67b4c2fa5) 执行 DCS 读取：`dev` 是主机设备，`channel` 是设备通道，[`cmd`](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615) 是 DCS 命令，`buf` 是读出数据的存储缓冲区，`len` 是接收缓冲区长度。成功返回读出数据大小，出错返回负值。

函数 [`mipi_dsi_dcs_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad0f324e32191469bc0d24ba203286237) 执行 DCS 写入：`dev`、`channel`、[`cmd`](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615) 含义同上，`buf` 是发送缓冲区，`len` 是发送缓冲区长度。成功返回写入数据大小，出错返回负值。

---

[上一章：MIPI显示总线接口](P245_MIPI显示总线接口.md) · [下一章：MIPI显示总线配置](P247_MIPI显示总线配置.md) · [返回大纲](大纲.md)
