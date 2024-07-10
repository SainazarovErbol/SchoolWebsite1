from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


docs = get_schema_view(
    openapi.Info(
        title="School website of Lenin High School No. 5",
        default_version='v1',
        description="Школьный сайт - ваш путь к упрощению взаимодействия с нашей школой. Здесь вы найдете информацию о наших мероприятиях, учебных планах, контактные данные и многое другое. Добро пожаловать!",
        terms_of_service="Предназначение нашего школьного сайта - обеспечить удобное взаимодействие всех заинтересованных лиц с жизнью школы. Здесь вы сможете получить доступ к актуальной информации о расписании занятий, событиях, успехах учащихся, контактам учителей и администрации, а также различным ресурсам, полезным для образовательного процесса. Наш сайт создан для того, чтобы делать взаимодействие с школой удобным, эффективным и простым для всех его пользователей.",
        contact=openapi.Contact(email="sh.erbol.2404@gmail.com"),
        license=openapi.License(name="MIT Lisence"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
