---
id: learning.zephyr-docs.external_modules.page-24
title: libmpix图像处理
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/libmpix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="libmpix"></a>
<a id="external-module-libmpix"></a>

# 第24章\_libmpix图像处理

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/libmpix.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 24.1\_简介（Introduction）

<a id="id3"></a>

[libmpix](https://github.com/libmpix/libmpix) 是用于微控制器图像数据处理的库，支持像素格式转换、拜耳阵列还原（Debayer）、模糊（Blur）、锐化（Sharpen）、颜色校正（Color Correction）、缩放（Resizing）等操作。

它把多个操作组成流水线（Pipeline），消除中间缓冲区，使资源受限系统可以处理更大分辨率，同时保持性能。

<a id="features"></a>

## 24.2\_特性（Features）

- 简单、零拷贝（Zero-copy）的流水线引擎，运行时开销较低。
- 降低内存开销；原文举例用5 kB随机存取存储器（Random Access Memory，RAM）处理1 MB数据。
- 支持POSIX系统（Linux／BSD／MacOS）以及Zephyr。

<a id="usage-with-zephyr"></a>

## 24.3\_在Zephyr中使用（Usage with Zephyr）

在原文 `west.yaml` 添加项目，或新建 `zephyr/submanifests/libmpix.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: libmpix
      url: https://github.com/libmpix/libmpix.git
      revision: main
      path: modules/lib/libmpix
```

API细节见libmpix头文件，简例为：

```c
#include <mpix/image.h>

struct mpix_image img;

mpix_image_from_buf(&img, buf_in, sizeof(buf_in), MPIX_FORMAT_RGB24);
mpix_image_kernel(&img, MPIX_KERNEL_DENOISE, 5);
mpix_image_kernel(&img, MPIX_KERNEL_SHARPEN, 3);
mpix_image_convert(&img, MPIX_FORMAT_YUYV);
mpix_image_to_buf(&img, buf_out, sizeof(buf_out));

return img.err;
```

> 译注——代码流程：从输入缓冲区构建RGB24图像，依次使用去噪（Denoise）和锐化核，转换成YUYV格式，再写入输出缓冲区，最后返回 `img.err`。输入／输出缓冲区由应用提供，这段是原文片段，不是独立完整应用；上面的内存数字也不是本批实测值。

<a id="references"></a>

## 24.4\_参考资料（References）


<a id="id2"></a>

1. [libmpix仓库](https://github.com/libmpix/libmpix)。


对应官方文档源码：[doc/develop/manifest/external/libmpix.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/libmpix.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/libmpix.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：工业IO库libiio](P023_工业IO库libiio.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：LuDLC数据链路协议](P025_LuDLC数据链路协议.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P023_工业IO库libiio.md) · [返回大纲](大纲.md) · [下一章](P025_LuDLC数据链路协议.md)

</details>

<!-- reading-navigation:end -->
