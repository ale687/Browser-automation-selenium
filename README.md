# 🕹️ Web Automation with Selenium (DemoQA)

Este proyecto es un ejemplo práctico de **automatización web con Selenium en Python**.  
El script automatiza un flujo completo dentro del sitio [DemoQA](https://demoqa.com/):

1. **Login automático** con credenciales de prueba.  
2. Navegación a la sección **Elements → Text Box**.  
3. **Rellenado y envío de formulario** con datos de usuario.  
4. Acceso a la sección **Upload and Download** y **descarga de archivo**.  

El proyecto está estructurado en una clase `WebAutomation`, lo que permite reutilizar y extender fácilmente sus funcionalidades.

---

## 🚀 Requisitos

- Python 3.9 o superior  
- Google Chrome instalado  
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible con tu versión de Chrome  

### Dependencias de Python

Instalar usando `pip`:

```bash
pip install selenium webdriver-manager
