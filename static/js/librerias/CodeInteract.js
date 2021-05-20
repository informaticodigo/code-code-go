// añadir ejecutador de código por el propio usuario
try{
    document.getElementById("ejecutar").addEventListener("click", ()=>{
        console.log(document.getElementById("codigo").value)
    })
}catch{
    try{
        document.getElementById("codigo").addEventListener("click", ()=>{
            console.log(document.getElementById("codigo").value)
        })
    }catch{
        try{
            document.getElementById("limpiar").addEventListener("click", ()=>{
                console.log(document.getElementById("codigo").value)
            })
        }catch{
            try{
                document.getElementById("doblar").addEventListener("click", ()=>{
                    console.log(document.getElementById("codigo").value)
                })
            }catch{
                if(true){
                    var integrated_code_editor = document.createElement("textarea");
                    integrated_code_editor.setAttribute("cols", 30);
                    integrated_code_editor.setAttribute("rows", 10);
                    integrated_code_editor.setAttribute("id", "codigo")
                    integrated_code_editor.style.width = "100%";
                    document.body.appendChild(integrated_code_editor);
                
                    var integrated_code_editor_boton1 = document.createElement("button");
                    //integrated_code_editor_boton1.setAttribute("value", "Ejecutar");
                    integrated_code_editor_boton1.setAttribute("id", "ejecutar")
                    //integrated_code_editor_boton1.style.width = "100%";
                    document.body.appendChild(integrated_code_editor_boton1);
                    document.getElementById("ejecutar").innerHTML = "Ejecutar"
                
                    var integrated_code_editor_boton3 = document.createElement("button");
                    //integrated_code_editor_boton3.setAttribute("value", "Doblar");
                    integrated_code_editor_boton3.setAttribute("id", "doblar")
                    //integrated_code_editor_boton3.style.width = "100%";
                    document.body.appendChild(integrated_code_editor_boton3);
                    document.getElementById("doblar").innerHTML = "Doblar"
                
                    var integrated_code_editor_boton2 = document.createElement("button");
                    //integrated_code_editor_boton2.setAttribute("value", "Limpiar");
                    integrated_code_editor_boton2.setAttribute("id", "limpiar")
                    //integrated_code_editor_boton2.style.width = "100%";
                    document.body.appendChild(integrated_code_editor_boton2);
                    document.getElementById("limpiar").innerHTML = "Limpiar"
                }
                
            }
        }
    }
}
try{
    document.getElementById("ejecutar").addEventListener("click", ()=>{
        eval(document.getElementById("codigo").value)
    })
}catch(TypeError){
    console.log("no hay elemento con id ejecutar")
}
try{
    document.getElementById("limpiar").addEventListener("click", ()=>{
        document.getElementById("codigo").value = ""
    })
}catch(TypeError){
    console.log("no hay elemento con id limpiar")
}
try{
    document.getElementById("doblar").addEventListener("click", ()=>{
        document.getElementById("codigo").value = document.getElementById("codigo").value + "\n" + document.getElementById("codigo").value
    })
}catch(TypeError){
    console.log("no hay elemento con id doblar")
}
try{
    document.getElementById("codigo").style.color = "#ffffff"
    document.getElementById("codigo").style.backgroundColor = "#000000"
    document.getElementById("codigo").addEventListener("keyup", ()=>{
        if(String(document.getElementById("codigo").value).endsWith("while+")){
            document.getElementById("codigo").value = String(document.getElementById("codigo").value).replace("while+", "") + 'while(condition){\n   \n}'
        }
        if(String(document.getElementById("codigo").value).endsWith("for+")){
            document.getElementById("codigo").value = String(document.getElementById("codigo").value).replace("for+", "") + 'for(let i = 0; i < 10; i++){\n    \n}'
        }
        if(String(document.getElementById("codigo").value).endsWith("function+")){
            document.getElementById("codigo").value = String(document.getElementById("codigo").value).replace("function+", "") + 'function NameOfFunction(number){\n     alert(number*number)\n}\n\nNameOfFunction(9)'
        }
        if(String(document.getElementById("codigo").value).endsWith("try+")){
            document.getElementById("codigo").value = String(document.getElementById("codigo").value).replace("try+", "") + 'try{\n     \n}catch(error){\n     \n}'
        }
    })
}catch(TypeError){
    console.log("no hay elemento con id codigo")
}