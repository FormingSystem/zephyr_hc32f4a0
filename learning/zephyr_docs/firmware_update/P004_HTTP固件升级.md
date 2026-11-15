---
id: learning.zephyr-docs.firmware_update.mgmt-http
title: HTTP固件升级
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/services/device_mgmt/fota_http.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_HTTP固件升级

原文：[Firmware Over-the-Air over HTTP](https://docs.zephyrproject.org/latest/services/device_mgmt/fota_http.html)。读取日期：2026-10-12，`latest`。

## 4.1\_直接下载到未运行的镜像槽

**基于HTTP的固件空中升级（Firmware Over-the-Air over Hypertext Transfer Protocol，FOTA HTTP）**库从服务器下载固件，直接写入当前未运行的 MCUboot 镜像槽。然后由应用选择请求交换、确认新镜像或擦除槽。它不使用 hawkBit、UpdateHub 一类设备管理协议，能提供文件的普通 Web 服务器即可作为来源，适用于简单部署和台架测试。

数据到达时通过 [Flash Image](P002_设备固件升级.md) 接口流式写入闪存，因此无需用**随机存取存储器（Random Access Memory，RAM）**保存完整镜像。目标槽随写入逐步擦除，并在第一个字节写入前清除 MCUboot **镜像尾部元数据（Trailer）**，避免把上一次镜像留下的状态误认为待执行的交换请求。

下载完成后，库从闪存读回 MCUboot 镜像头；数据不是合法镜像时返回错误 `-ENOEXEC`。**库本身不验证签名**，真正启动前由 MCUboot 验证，并据此决定能否运行。

启用 Kconfig 配置项 [`CONFIG_FOTA_HTTP_SHA256_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_SHA256_CHECK) 后，可将下载数据与调用方提供的 **安全散列算法256位摘要（Secure Hash Algorithm 256-bit，SHA-256）**比较，在重启前发现传输损坏。摘要不匹配或后文降级检查拒绝的镜像会从槽中擦除。若下载中途失败，函数 [`fota_http_apply()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaad1653d95d0d798c63e2d4b3f9ff9324) 会拒绝应用这个槽，直到再次下载成功；部分数据保留，用于断点续传。

> 译注：摘要比较与数字签名验证承担不同职责，摘要的来源也需可信；本章描述库与 MCUboot 的分工，不表示下载函数成功就已经完成可信引导。是否支持这些接口应核对当前源码版本；本页依据读取日期对应的官方 latest 文档。

## 4.2\_典型升级顺序

1. 函数 [`fota_http_download()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga8aa13892a735e7f2826c00dab36b0a08) 或 [`fota_http_download_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaf730ea430346720f05dd7f290eef69c6) 把镜像取到次槽。结构体 [`fota_http_download_params`](https://docs.zephyrproject.org/latest/doxygen/html/structfota__http__download__params.html) 中可选的 `sha256`、`resume` 和**传输层安全（Transport Layer Security，TLS）**字段，仅在相应 Kconfig 功能启用时存在。
2. 函数 `fota_http_apply()` 把镜像标记为试启动或永久启动。
3. 设备重启，MCUboot 执行镜像交换。
4. 试启动时，应用自检后调用函数 [`fota_http_confirm()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gab3d4aa4a5842bf739e4554a40e8b4db5) 确认。没有确认，下一次重启时 MCUboot 会回退到旧镜像。

回退要求 MCUboot 选择支持回退的模式，例如 swap-using-move（移动交换）或 swap-using-offset（偏移交换）。overwrite-only（仅覆盖）模式会覆盖旧镜像，确认操作不能恢复它；应核对板卡 sysbuild 配置选定的模式。

试镜像运行期间，次槽保存着可能回退使用的镜像。在应用确认前，下载函数返回 `-EPERM` 拒绝覆盖它。

## 4.3\_线程、栈与取消

同步下载函数在整个传输期间阻塞调用线程，需要足够栈空间运行 HTTP 客户端；使用**安全超文本传输协议（Hypertext Transfer Protocol Secure，HTTPS）**时还要承担 TLS 握手。

启用 Kconfig 配置项 [`CONFIG_FOTA_HTTP_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_ASYNC) 后，异步下载函数由库自己的线程执行，并通过完成回调报告结果，线程栈由 [`CONFIG_FOTA_HTTP_THREAD_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_THREAD_STACK_SIZE) 设置。命令行下载使用异步形式，因此下载工作不依赖命令行线程栈大小。只使用同步函数的应用可关闭异步选项，避免分配额外线程栈。

同一时间只运行一次下载。函数 [`fota_http_cancel()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac67bbc767cf189830d071651b6b5d986) 请求取消正在进行的传输；在收到下一个数据片段或请求超时时才实际中止，并非保证立即返回全部网络资源。

## 4.4\_重定向与断点续传

状态码 301、302、303、307、308 会触发跟随重定向，最多跟随 Kconfig 配置项 [`CONFIG_FOTA_HTTP_MAX_REDIRECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_MAX_REDIRECTS) 指定次数。支持绝对**统一资源定位符（Uniform Resource Locator，URL）**和只含路径的 `Location` 响应头。

启用 [`CONFIG_FOTA_HTTP_RESUME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_RESUME) 后，传输过程中和失败时会把下载偏移保存到设置存储。后续请求设置参数 `resume`，库使用 HTTP **范围请求（Range Request）**从断点继续，但只有 URL 和镜像索引都与中断的下载一致时才复用偏移。

如果服务器此前发送过实体标签响应头 `ETag` 或修改时间响应头 `Last-Modified`，续传请求会通过 `If-Range` 携带它，使服务器文件变化时从头下载。服务器忽略 `Range`、直接返回完整文件时，也从零开始；返回 `416 Range Not Satisfiable` 时同样重启传输，这可能发生在文件变短、旧偏移超出范围时。校验标识过长而无法保存时，库也丢弃进度，避免针对可能已改变的文件继续拼接。镜像下载完整后清除保存的偏移。

## 4.5\_多个镜像与直接执行模式

具有多个可更新镜像的布局，使用参数 `image_index` 指定下载到哪一个次槽。应用和确认函数也接收同一索引，使含有第二个设备固件的系统只确认本设备实际验证过的镜像。

多个镜像必须配套运行时，先下载并为每个镜像请求应用，再重启；MCUboot 验证整个集合后统一切换。之后仍须逐一确认，遗漏确认的镜像会独立回退。

函数 [`fota_http_confirm_pending()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f4caeac9e7f14e24da6d403b4730ded) 只报告镜像 0，其他镜像的确认状态由多镜像应用自行跟踪。Kconfig 配置项 [`CONFIG_FOTA_HTTP_REJECT_DOWNGRADE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_REJECT_DOWNGRADE) 提供的降级检查也只覆盖镜像 0。

**直接原位执行（Direct Execute-in-Place，Direct-XIP）**模式下，镜像运行槽在链接时固定，因此设备须下载为当前空闲槽构建的镜像版本。函数 [`fota_http_get_download_slot()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f0b137c19a30942725406abdcf89497) 返回该槽。这仅支持单镜像布局：除第一组镜像之外，库总是上传到配对槽中奇数编号的槽，适合交换与覆盖模式，不适合多镜像 Direct-XIP。

## 4.6\_降级保护

启用 `CONFIG_FOTA_HTTP_REJECT_DOWNGRADE` 后，下载镜像头中的版本会与正在运行的版本比较；较旧版本使下载失败并被擦除，避免误用。

原文强调这只是应用的便捷检查。必须强制执行的版本策略应放在引导程序中，结合 MCUboot 的降级阻止与硬件回滚保护选项。

## 4.7\_TLS连接与证书

启用 Kconfig 配置项 [`CONFIG_FOTA_HTTP_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS) 后接受 HTTPS 地址。服务器的**证书颁发机构（Certificate Authority，CA）**证书，通过 [`CONFIG_FOTA_HTTP_TLS_SEC_TAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS_SEC_TAG) 或下载参数中的安全标签查找；可由函数 [`fota_http_tls_add_ca()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga511dd696af7bd7b61a9924ca64964f32) 注册，也可直接使用函数 [`tls_credential_add()`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7)。使用**双向TLS（Mutual TLS）**时，通过函数 [`fota_http_tls_add_client_cert()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gacdeabce6009b1b1b9b10cfe6fe9fd9d9) 注册客户端证书和私钥。

默认要求验证对端，生产环境应保持 [`CONFIG_FOTA_HTTP_TLS_PEER_VERIFY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS_PEER_VERIFY) 的默认设置。库把 URL 中的主机名与证书匹配；如果 URL 使用**互联网协议（Internet Protocol，IP）**地址，而证书没有匹配条目，可通过参数 `tls_hostname` 提供预期主机名。

仅启用 [`CONFIG_MBEDTLS_HAVE_TIME_DATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HAVE_TIME_DATE) 时才强制检查证书有效期，设备必须在第一次下载前已有正确的现实时间。Kconfig 配置项 [`CONFIG_FOTA_HTTP_TLS_VERSION_1_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS_VERSION_1_3) 可选择 TLS 1.3。

## 4.8\_控制台命令与参考

启用 Kconfig 配置项 [`CONFIG_FOTA_HTTP_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_SHELL) 后，控制台命令 `fota` 暴露相应能力。以下保留原帮助文字与参数形式：

```text
fota download <url> [resume] [image=<n>]   download an image
fota cancel                                abort the download in progress
fota apply [permanent] [image=<n>]         boot the downloaded image on the next reset
fota confirm [image]                       confirm the running image
fota status                                show images and confirmation state
fota erase [image]                         erase the secondary slot
```

其中 download（下载）把文件写入目标槽，cancel（取消）中止进行中的下载，apply（应用）使下次复位尝试启动下载镜像，confirm（确认）确认当前运行镜像，status（状态）显示镜像和确认状态，erase（擦除）清除次槽。参数 `permanent` 请求永久启动，`image` 选择镜像索引，`resume` 请求续传。

完整流程见 [HTTP固件升级示例](P023_HTTP固件升级示例.md)，完整**应用程序编程接口（Application Programming Interface，API）**见 [FOTA HTTP参考](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html)。本次未调用下载、应用、擦除或重启命令。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：空中升级](P003_空中升级.md) · [本模块主线目录](../reading/firmware_update.md) · [全部主线](../reading/README.md) · [下一篇：镜像签名](P005_镜像签名.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：空中升级](P003_空中升级.md) · [下一章：镜像签名](P005_镜像签名.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
