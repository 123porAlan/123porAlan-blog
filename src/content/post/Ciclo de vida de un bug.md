---
title: "El ciclo de vida de un bug"
description: "Conoce cada etapa del ciclo de vida de un bug, desde su detección hasta su cierre, y los responsables clave en el proceso."
publishDate: "13 May 2025"
tags: ["Testing101", "SoftwareTesting", "Computación"]
draft: false
seriesId: citrus-docs
orderInSeries: 4
---
# **El Ciclo de Vida de un Bug: Etapas, Roles y Buenas Prácticas**  

El ciclo de vida de un bug es el proceso estructurado que sigue un defecto desde su detección hasta su resolución definitiva. Cada etapa implica acciones específicas y roles claramente definidos para garantizar una gestión eficiente y una solución efectiva. A continuación, te detallo cada fase con mayor profundidad, incluyendo buenas prácticas y flujos alternativos.  

---  

## **1. Nuevo (New)**  
**Responsable**: Tester o QA Engineer  
**Descripción**:  
El tester identifica un comportamiento inesperado o inconsistente durante la ejecución de pruebas (manuales o automatizadas) y lo reporta en el sistema de seguimiento de bugs.  

**Acciones Clave**:  
✔ **Documentación detallada**:  
   - Pasos exactos para reproducir el defecto.  
   - Entorno de prueba (navegador, SO, versión del software, etc.).  
   - Comportamiento **esperado** vs. **comportamiento actual**.  
   - Capturas de pantalla, logs o videos si son relevantes.  

✔ **Clasificación del bug**:  
   - **Prioridad** (Urgente, Alta, Media, Baja): Impacto en el negocio o usuario.  
   - **Severidad** (Crítico, Mayor, Medio, Menor): Grado de afectación al sistema.  

✔ **Asignación inicial**:  
   - El bug se registra como "Nuevo" y se asigna al líder de desarrollo o project manager para su revisión.  

---  

## **2. Asignado (Assigned)**  
**Responsable**: Líder de Desarrollo o Project Manager  
**Descripción**:  
El bug es evaluado para determinar su validez y asignado al desarrollador correspondiente.  

**Acciones Clave**:  
✔ **Validación inicial**:  
   - Confirmar si el bug es **reproducible** y no está duplicado.  
   - Verificar si es un defecto real o un malentendido (ej: error de configuración).  

✔ **Decisiones posibles**:  
   - **Aceptar**: Asignar al desarrollador para su corrección.  
   - **Rechazar**: Si no es un bug válido (ej: comportamiento esperado, error del usuario).  
   - **Posponer**: Si no es crítico y se abordará en una futura iteración.  

---  

## **3. Activo (Active / In Progress)**  
**Responsable**: Desarrollador  
**Descripción**:  
El desarrollador investiga y corrige el defecto.  

**Acciones Clave**:  
✔ **Análisis de la causa raíz**:  
   - Revisar el código, logs y flujos relacionados.  
   - Identificar si el error es propio del desarrollo, de integración o de un componente externo.  

✔ **Desarrollo de la solución**:  
   - Implementar el fix y probarlo localmente.  
   - Asegurar que no introduce nuevos defectos (pruebas unitarias).  

✔ **Actualización del estado**:  
   - Documentar los cambios realizados en el sistema de seguimiento.  

---  

## **4. Arreglado (Fixed / Resolved)**  
**Responsable**: Desarrollador  
**Descripción**:  
El desarrollador confirma que el bug ha sido corregido y lo envía para verificación.  

**Acciones Clave**:  
✔ **Subir cambios al repositorio**:  
   - Realizar commit con una descripción clara (ej: "Fix #123: Corrección de error en cálculo de impuestos").  
   - Fusionar en la rama correspondiente (develop, main, etc.).  

✔ **Marcar como "Fixed" en el sistema**:  
   - Indicar la versión donde se aplicó el fix.  
   - Proporcionar detalles adicionales si el tester necesita validar algo específico.  

---  

## **5. Verificado (Verified / Closed)**  
**Responsable**: Tester  
**Descripción**:  
El QA verifica que la corrección sea efectiva y que no genere regresiones.  

**Acciones Clave**:  
✔ **Pruebas de regresión**:  
   - Validar el escenario original del bug.  
   - Asegurar que funcionalidades relacionadas no se vean afectadas.  

✔ **Resultados posibles**:  
   - **Éxito**: El bug pasa a estado "Cerrado".  
   - **Fallo**: Se reabre y se devuelve a "Activo" con comentarios detallados.  

---  

## **6. Cerrado (Closed)**  
**Responsable**: Tester o Líder de QA  
**Descripción**:  
El bug se cierra definitivamente al confirmar su resolución.  

**Acciones Clave**:  
✔ **Documentación final**:  
   - Registrar evidencia de la prueba exitosa.  
   - Actualizar reportes de calidad del proyecto.  

✔ **Archivado**:  
   - El bug queda como referencia para auditorías o análisis futuros.  

---  

## **7. Rechazado (Rejected)**  
 **Responsable**: Líder de Desarrollo o QA Manager  
**Descripción**:  
El bug es descartado por no ser válido (duplicado, no reproducible, error de usuario, etc.).  

**Acciones Clave**:  
✔ **Justificación clara**:  
   - Ejemplo: "No es un defecto, el comportamiento es el esperado según el requerimiento X".  

✔ **Comunicación con el tester**:  
   - Si el bug fue malinterpretado, se aclara el escenario para evitar reportes similares.  

---  

## **Flujos Alternativos y Consideraciones**  
 🔄 **Reapertura de un Bug**  
- Si el fix no funciona, el bug vuelve a **"Activo"** con observaciones detalladas.  
- Si se encuentra el mismo defecto en otra área, se crea un **nuevo reporte** vinculado al original.  

⚠ **Bugs Duplicados o Invalidados**  
- Se marcan como **"Rechazado"** o **"Duplicado"** y se enlazan al bug principal.  

🛠 **Buenas Prácticas**  
✔ **Comunicación constante** entre Devs y QA para evitar malentendidos.  
✔ **Seguimiento con herramientas** como Jira, Azure DevOps o Bugzilla para mantener trazabilidad.  
✔ **Retrospectivas** para analizar bugs recurrentes y mejorar procesos.  

---  

**Conclusión**  
Un ciclo de vida de bugs bien gestionado mejora la calidad del software, optimiza el tiempo del equipo y facilita la entrega de productos más estables. La clave está en la **documentación clara**, la **colaboración entre roles** y el **uso de herramientas adecuadas**.  

