#include <QTimer>
#include <QCoreApplication>
#include <AppImageUpdaterBridge>

using namespace AppImageUpdaterBridge;

int main(int argc, char** argv) {
    QCoreApplication app(argc, argv);
    AppImageDeltaRevisioner DeltaRevisioner;
    QObject::connect(&DeltaRevisioner, &AppImageDeltaRevisioner::finished, &app, &QCoreApplication::quit);
    DeltaRevisioner.setShowLog(true);
    DeltaRevisioner.start();

    QTimer::singleShot(10, &app, &QCoreApplication::quit);
    return app.exec();
}
