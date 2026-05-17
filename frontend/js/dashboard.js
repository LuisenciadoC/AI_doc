<!-- dashboard.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Docky AI</title>

    <link rel="stylesheet" href="../css/dashboard.css">
</head>
<body>

<div class="dashboard_container">

    <!-- SIDEBAR -->
    <aside class="sidebar">

        <div class="profile">

            <img 
                src="../assets/images/user.png"
                alt="Usuario"
            >

            <h3 id="userName">
                Usuario
            </h3>

            <p id="userRole">
                Rol
            </p>

        </div>

        <nav class="menu">

            <a href="dashboard.html">
                Inicio
            </a>

            <a href="documents.html">
                Documentos
            </a>

            <a href="users.html">
                Usuarios
            </a>

            <a href="ai_chat.html">
                IA
            </a>

        </nav>

        <button class="logout_button" onclick="logout()">
            Cerrar sesión
        </button>

    </aside>

    <!-- CONTENIDO -->
    <main class="main_content">

        <header class="topbar">

            <h1>
                Bienvenido
            </h1>

        </header>

        <!-- RESUMEN -->
        <section class="summary">

            <div class="card">
                <h3>Total documentos</h3>
                <p id="totalDocuments">0</p>
            </div>

            <div class="card">
                <h3>Documentos activos</h3>
                <p id="activeDocuments">0</p>
            </div>

            <div class="card">
                <h3>Documentos eliminados</h3>
                <p id="deletedDocuments">0</p>
            </div>

        </section>

        <!-- TABLA -->
        <section class="table_section">

            <div class="table_header">

                <h2>
                    Últimos documentos
                </h2>

                <button onclick="goToCreate()">
                    + Nuevo
                </button>

            </div>

            <table>

                <thead>

                    <tr>
                        <th>Código</th>
                        <th>Título</th>
                        <th>Estado</th>
                        <th>Acciones</th>
                    </tr>

                </thead>

                <tbody id="documentsTable">

                </tbody>

            </table>

        </section>

    </main>

</div>

<script src="../js/dashboard.js"></script>

</body>
</html>