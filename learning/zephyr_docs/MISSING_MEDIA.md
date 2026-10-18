---
id: learning.zephyr-docs.missing-media
title: 已译正文与缺失原始媒体清单
kind: reference
status: evolving
domains: [zephyr, documentation, media]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 已译正文与缺失原始媒体清单

**固定范围中的 16336 个适用官方页面正文均已翻译。16331 页完整完成；以下 5 页尚缺 8 个不同的原始图片文件，涉及 13 处原始引用，因此整套媒体交付尚未完成。** 另有 1 个官方 404 错误页不适用。

2026-10-18 已通过正常浏览器访问原始地址，取回 6 张 eLinux 原图并校验有效文件、尺寸、字节数与 SHA-256；H3ULCB 与 Spider 两页由此完整完成。剩余 7 个地址返回 HTTP 404，1 个返回 HTTP 403；Cytron 浏览器访问仍停留在安全验证页，Longan 浏览器访问返回响应失败。没有把错误页保存为图片。机器可读记录见 [missing-media.json](missing-media.json)。

## 尚缺原图的已译页面

| 官方页面 | 本地完整译文 | 缺失原文件数 |
| --- | --- | ---: |
| [Motion 2350 Pro](https://docs.zephyrproject.org/latest/boards/cytron/motion_2350_pro/doc/index.html) | [阅读译文](boards_pending_media/P001_Motion_2350_Pro.md) | 1 |
| [CANBed RP2040](https://docs.zephyrproject.org/latest/boards/longan/canbed_rp2040/doc/index.html) | [阅读译文](boards_pending_media/P002_CANBed_RP2040.md) | 1 |
| [bmp581_8h](https://docs.zephyrproject.org/latest/doxygen/html/bmp581_8h.html) | [阅读译文](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md) | 5 |
| [group__bmp581__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html) | [阅读译文](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | 5 |
| [group__scd4x__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html) | [阅读译文](api_pending_media_reference/P003_SCD4X扩展传感器接口.md) | 1 |

## 原始文件缺项

| 原始文件 | 涉及页面 | 当前取得结果 |
| --- | --- | --- |
| [form_0.png](https://docs.zephyrproject.org/latest/doxygen/html/form_0.png) | [P003_SCD4X扩展传感器接口](api_pending_media_reference/P003_SCD4X扩展传感器接口.md) | HTTP 404 |
| [form_1.png](https://docs.zephyrproject.org/latest/doxygen/html/form_1.png) | [P001_BMP581设备树常量头文件参考](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md)、[P002_BMP581扩展传感器接口](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | HTTP 404 |
| [form_2.png](https://docs.zephyrproject.org/latest/doxygen/html/form_2.png) | [P001_BMP581设备树常量头文件参考](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md)、[P002_BMP581扩展传感器接口](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | HTTP 404 |
| [form_3.png](https://docs.zephyrproject.org/latest/doxygen/html/form_3.png) | [P001_BMP581设备树常量头文件参考](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md)、[P002_BMP581扩展传感器接口](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | HTTP 404 |
| [form_4.png](https://docs.zephyrproject.org/latest/doxygen/html/form_4.png) | [P001_BMP581设备树常量头文件参考](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md)、[P002_BMP581扩展传感器接口](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | HTTP 404 |
| [form_5.png](https://docs.zephyrproject.org/latest/doxygen/html/form_5.png) | [P001_BMP581设备树常量头文件参考](api_pending_media_reference/P001_BMP581设备树常量头文件参考.md)、[P002_BMP581扩展传感器接口](api_pending_media_reference/P002_BMP581扩展传感器接口.md) | HTTP 404 |
| [pinout-diagram-motion-2350-pro3.png](https://static.cytron.io/image/catalog/products/MOTION-2350-PRO/pinout-diagram-motion-2350-pro3.png) | [P001_Motion_2350_Pro](boards_pending_media/P001_Motion_2350_Pro.md) | HTTP 403；浏览器停留在安全验证页 |
| [Details_of_CANBed-04.png](https://www.longan-labs.cc/media/wysiwyg/CAN-Bus/CANBed/Details_of_CANBed-04.png) | [P002_CANBed_RP2040](boards_pending_media/P002_CANBed_RP2040.md) | HTTP 404 |

## 本次补齐的原始图片

六张图片均从 Zephyr 原文指定的 eLinux URL 下载，未改动字节、分辨率或格式。正文原引用位置已改为相对路径显示原图，点击可打开完整尺寸；[原图清单](official-images.json)保留各自来源、摘要及引用页面。

| 原始文件 | 本地原件 |
| --- | --- |
| [Kfisher_bot_specs.png](https://elinux.org/images/0/06/Kfisher_bot_specs.png) | [查看原图](boards_pending_media/images/Kfisher_bot_specs.png) |
| [Kfisher_top_specs.png](https://elinux.org/images/0/08/Kfisher_top_specs.png) | [查看原图](boards_pending_media/images/Kfisher_top_specs.png) |
| [R-Car-H3-topview.jpg](https://elinux.org/images/1/1f/R-Car-H3-topview.jpg) | [查看原图](boards_pending_media/images/R-Car-H3-topview.jpg) |
| [R-Car-H3-bottomview.jpg](https://elinux.org/images/c/c2/R-Car-H3-bottomview.jpg) | [查看原图](boards_pending_media/images/R-Car-H3-bottomview.jpg) |
| [Rcar_s4_spider_breakout_board.jpg](https://elinux.org/images/2/29/Rcar_s4_spider_breakout_board.jpg) | [查看原图](boards_pending_media/images/Rcar_s4_spider_breakout_board.jpg) |
| [Rcar_s4_spider_cpu_board.jpg](https://elinux.org/images/6/6d/Rcar_s4_spider_cpu_board.jpg) | [查看原图](boards_pending_media/images/Rcar_s4_spider_cpu_board.jpg) |

H3ULCB 与 Kingfisher 图片见 [R-Car H3ULCB 译文](boards_pending_media/P003_R-Car_H3ULCB.md)；Spider 两张图片见 [R-Car Spider 译文](boards_pending_media/P004_R-Car_Spider.md)。

## 已保留的材料

- 原先四份开发板页面直接嵌入的四张 Zephyr 官网原图已全部保留；本次补齐其外链引用中的六张原图。
- Motion 2350 Pro 与 CANBed RP2040 另附厂商官方仓库的同型号原始引脚／接口图，文件未改动；尚不能证明与 Zephyr 引用的失效文件字节相同，因此仍保留两项原始缺项。见[厂商补充图片清单](supplementary-manufacturer-images.json)。
- 三份 API 页的六个公式 PNG 尚未取得。官方 HTML 原始替代文本（alt）和 LaTeX 公式完整保留；两份 BMP581 页共用五个 PNG，SCD4X 页引用一个 PNG，共十一处引用。详见[公式来源记录](api_pending_media_reference/formula-sources.json)。
- 已有 GIF、SVG、HTML 动画及适配文件保持原位；没有用生成截图冒充原件。

公开归档可用性查询在本次复查中仍返回 HTTP 429。尚未取得的文件不会计入已下载原图。

[返回翻译集](README.md) · [官方扩展参考](reference_library/README.md) · [全站进度](PROGRESS.md)
