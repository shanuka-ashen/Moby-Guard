.class Lcom/shanuka/signaturedetector/FirstFragment$4;
.super Ljava/lang/Object;
.source "FirstFragment.java"

# interfaces
.implements Landroid/content/DialogInterface$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/shanuka/signaturedetector/FirstFragment;->onResume()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/shanuka/signaturedetector/FirstFragment;


# direct methods
.method constructor <init>(Lcom/shanuka/signaturedetector/FirstFragment;)V
    .locals 0
    .param p1, "this$0"    # Lcom/shanuka/signaturedetector/FirstFragment;

    .line 225
    iput-object p1, p0, Lcom/shanuka/signaturedetector/FirstFragment$4;->this$0:Lcom/shanuka/signaturedetector/FirstFragment;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/content/DialogInterface;I)V
    .locals 1
    .param p1, "dialog"    # Landroid/content/DialogInterface;
    .param p2, "which"    # I

    .line 227
    iget-object v0, p0, Lcom/shanuka/signaturedetector/FirstFragment$4;->this$0:Lcom/shanuka/signaturedetector/FirstFragment;

    invoke-virtual {v0}, Lcom/shanuka/signaturedetector/FirstFragment;->requireActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroidx/fragment/app/FragmentActivity;->finish()V

    .line 228
    return-void
.end method
