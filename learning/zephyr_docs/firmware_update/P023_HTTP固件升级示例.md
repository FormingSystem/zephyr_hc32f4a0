---
id: learning.zephyr-docs.firmware_update.mgmtex-fota-http
title: HTTP固件升级示例
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/mgmt/fota_http/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="fota-http"></a>

# 第23章\_HTTP固件升级示例

原文：[Firmware Over-the-Air over HTTP](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/fota_http/README.html)。读取日期：2026-10-13，`latest`。

## 23.1\_HTTP升级示例与要求

本示例使用[HTTP固件升级库](P004_HTTP固件升级.md)，通过 **超文本传输协议（Hypertext Transfer Protocol，HTTP）**的GET请求下载签名固件，流式写入MCUboot当前未运行的槽，再请求引导加载程序启动该镜像。只需一个能提供目录内容的HTTP服务器，无需额外升级服务或设备管理协议。

**空中固件升级（Firmware Over-The-Air，FOTA）**流程可通过示例启用的 `fota` **命令解释器（Shell）**命令完成。要求开发板有网络接口、MCUboot的双应用槽分区，以及设备可访问的HTTP服务器。

示例用 **系统构建（System Build，sysbuild）**同时构建和烧录MCUboot；引导程序使用偏移交换（Swap Using Offset）模式，以测试回退路径。仅覆盖（Overwrite Only）模式不支持回退。

**原文警告：**默认使用MCUboot仓库公开的开发签名密钥，任何人都能用它签名。实际设备应在MCUboot配置中通过Kconfig配置项 [`CONFIG_MCUBOOT_SIGNATURE_KEY_FILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_SIGNATURE_KEY_FILE) 指定自己的密钥。

## 23.2\_构建两个版本

从Zephyr源码目录构建并烧录初始版本1.0.0，以便在控制台区分；CMake命令行参数 `-DCONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION` 为镜像签名指定版本字符串：

```shell
west build -b esp32c5_devkitc/esp32c5/hpcore --sysbuild samples/subsys/mgmt/fota_http -- -DCONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION=\"1.0.0\"
west flash
```

再构建版本2.0.0，保留其构建目录供设备下载：

```shell
west build -b esp32c5_devkitc/esp32c5/hpcore --sysbuild -d build/build-v2 samples/subsys/mgmt/fota_http -- -DCONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION=\"2.0.0\"
```

原命令的板卡为ESP32-C5，不能直接替代为尚未具备联网和双槽配置的HC32板。`--` 后面的带引号Kconfig字符串按原Shell命令保留；使用其他主机Shell时须检查实际传入CMake的引号。

在主机提供签名文件，原文命令为：

```shell
cd build-v2/fota_http/zephyr && python3 -m http.server 8000 --bind 0.0.0.0
```

> 译注：上一步实际创建 `build/build-v2`，此处却写成 `build-v2`。若仍位于源码目录，应先进入 `build/build-v2/fota_http/zephyr`，再运行HTTP服务器；原命令只在已进入 `build` 后路径相符。服务器运行期间需要另一个终端继续操作。MCUboot要求上传 `zephyr.signed.bin`，不能用未签名的 `zephyr.bin`。

## 23.3\_联网、下载与试启动

Wi-Fi板先联网，替换命令中的网络名、口令和密钥管理占位符：

```shell
uart:~$ wifi connect -s <ssid> -p <passphrase> -k <key_mgmt>
```

以太网板在启动时通过 **动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）**取得地址。以下均为设备Shell命令，`uart:~$` 是提示符，不是输入内容；`<host-ip>` 替换成设备可达的服务器 **互联网协议（Internet Protocol，IP）**地址：

```shell
uart:~$ fota download http://<host-ip>:8000/zephyr.signed.bin
uart:~$ fota apply
uart:~$ kernel reboot cold
```

重启后，控制台应显示2.0.0作为测试镜像运行。若不确认，下次重启会回退到1.0.0；检查并确认：

```shell
uart:~$ fota status
uart:~$ fota confirm
```

命令变体 `fota apply permanent` 跳过测试启动，立即把镜像安排为永久确认。

## 23.4\_自动下载

Kconfig配置项 `CONFIG_SAMPLE_FOTA_HTTP_AUTO_URL` 指定自动下载地址。示例注册连接管理器的 **第四层连接事件（Layer 4 Connected Event，L4）**，接口具有地址后调用函数 [`fota_http_download_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaf730ea430346720f05dd7f290eef69c6)，并打印库线程报告的进度：

```shell
west build -b frdm_k64f --sysbuild samples/subsys/mgmt/fota_http -- -DCONFIG_SAMPLE_FOTA_HTTP_AUTO_URL=\"http://<host-ip>:8000/zephyr.signed.bin\"
```

Wi-Fi板在 `wifi connect` 成功后开始下载。自动下载仅存储镜像，仍须 `fota apply` 才安排启动。当前镜像仍为测试镜像时跳过下载，因为另一个槽保存回退镜像；次槽已包含当前运行版本时也跳过。

使用 `resume.conf` 配置片段后，被复位中断的传输可在下次启动时从上次保存偏移继续。

## 23.5\_断点续传

构建时加入Kconfig片段 `resume.conf`，将下载偏移存入设置。断电或网络错误后带 `resume` 重新下载，使用HTTP范围请求（Range Request）：

```shell
uart:~$ fota download http://<host-ip>:8000/zephyr.signed.bin resume
```

服务器不支持范围请求时会返回整个文件，下载重新从零开始。片段按[应用配置](https://docs.zephyrproject.org/latest/develop/application/index.html#important-build-vars)通过 `EXTRA_CONF_FILE` 加入；这些相对文件位于示例应用目录。

## 23.6\_TLS与证书

Kconfig片段 `tls.conf` 启用 **传输层安全（Transport Layer Security，TLS）**，接受HTTPS地址。示例把 `src/ca_cert.pem` 内的 **隐私增强邮件编码（Privacy-Enhanced Mail，PEM）**证书注册为受信任 **证书颁发机构（Certificate Authority，CA）**；构建时将证书转换为C数组，由 `src/main.c` 引入。

默认是用于 `localhost` 和 `127.0.0.1` 的自签名测试证书，仅供演示代码路径。提供实际镜像前，应换成服务器证书或签发它的CA证书。

原文在主机上用OpenSSL为主机地址生成自签名证书，再用 `server.pem` 替换示例的 `src/ca_cert.pem`：

```shell
openssl req -x509 -newkey rsa:2048 -nodes -keyout server.key \
  -out server.pem -days 365 -subj "/CN=<host-ip>" \
  -addext "subjectAltName=IP:<host-ip>"
```

> 译注：这里的 `<host-ip>` 必须替换为实际服务器IP，证书主题备用名称也要匹配。内置证书改变后须重新构建固件。命令使用Unix Shell续行符，不能把反斜杠续行直接当作PowerShell语法。

从存有签名镜像的目录运行以下Python HTTPS服务器：

```python
import http.server, ssl
httpd = http.server.HTTPServer(("0.0.0.0", 8443),
                               http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("server.pem", "server.key")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
```

证书和密钥文件需能按程序中的相对文件名找到；若生成在其他目录，应先放到正确位置或调整相对路径。程序中的 **安全套接层（Secure Sockets Layer，SSL）**模块名沿用Python历史命名，此处实际创建TLS服务器上下文。

证书也可在运行时通过配置已启用的TLS凭据Shell设置：

```shell
uart:~$ cred add 1 CA DEFAULT strt <PEM certificate>
```

`<PEM certificate>` 是证书内容占位符。只有启用Kconfig配置项 [`CONFIG_MBEDTLS_HAVE_TIME_DATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HAVE_TIME_DATE) 才检查证书有效期，此时首次下载前必须建立正确的设备实时时间。

进一步参阅[FOTA HTTP接口](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html)。

[上一章：SMP服务器示例](P022_SMP服务器示例.md) · [下一章：hawkBit升级示例](P024_hawkBit升级示例.md) · [返回大纲](大纲.md)
